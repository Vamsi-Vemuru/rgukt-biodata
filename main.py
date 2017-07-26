#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.ext import ndb
from google.appengine.api import users


import webapp2
import jinja2
import os
import logging
import datetime
import pytz
from dateutil import parser
import csv

JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions=['jinja2.ext.autoescape'],
	autoescape=True)

admins = ["sirimala.sreenath@gmail.com", "ss@fju.us", "pg@fju.us", "vamsi0493@gmail.com", "praveeng1503@gmail.com"]

#create a local timezone (Indian Standard Time)
IST = pytz.timezone('Asia/Kolkata')

def _now_ist():
	return datetime.datetime.now(IST)

class BioData(ndb.Model):
	rgukt_id = ndb.StringProperty()
	first_name = ndb.StringProperty()
	middle_name = ndb.StringProperty()
	last_name = ndb.StringProperty()
	mobile = ndb.StringProperty()
	email = ndb.StringProperty()
	skype = ndb.StringProperty()
	school_name = ndb.StringProperty()
	class_rank = ndb.StringProperty()
	cgpa = ndb.StringProperty()
	father_name = ndb.StringProperty()
	mother_name = ndb.StringProperty()
	annual_family_income = ndb.StringProperty()
	caste = ndb.StringProperty()
	address1 = ndb.StringProperty()
	address2 = ndb.StringProperty()
	zipcode = ndb.StringProperty()
	started_on = ndb.DateTimeProperty()
	date_of_graduation = ndb.StringProperty()
	dob_day = ndb.StringProperty()
	dob_month = ndb.StringProperty()
	dob_year = ndb.StringProperty()
	father_annual_income = ndb.StringProperty()
	father_highest_education = ndb.StringProperty()
	father_occupation = ndb.StringProperty()
	gender = ndb.StringProperty()
	mother_annual_income = ndb.StringProperty()
	mother_highest_education = ndb.StringProperty()
	mother_occupation = ndb.StringProperty()
	submitted_on = ndb.DateTimeProperty(auto_now=True)

def _convert_string_to_date(str_date):
	return parser.parse(str_date).replace(tzinfo=None)

class BakMainHandler(webapp2.RequestHandler):
	def get(self):
		template = JINJA_ENVIRONMENT.get_template('form.html')
		logging.info(template)
		self.response.out.write(template.render({'datetime':datetime.datetime.now()}))
	def post(self):
		# form_items = self.request.POST.items()
		rgukt_id = self.request.POST["rgukt_id"]
		first_name = self.request.POST["first_name"]
		middle_name = self.request.POST["middle_name"]
		last_name = self.request.POST["last_name"]
		mobile = self.request.POST["mobile"]
		email = self.request.POST["email"]
		skype = self.request.POST["skype"]
		school_name = self.request.POST["school_name"]
		class_rank = self.request.POST["class_rank"]
		cgpa = self.request.POST["cgpa"]
		father_name = self.request.POST["father_name"]
		father_annual_income = self.request.POST["father_annual_income"]
		mother_annual_income = self.request.POST["mother_annual_income"]
		mother_name = self.request.POST["mother_name"]
		mother_occupation = self.request.POST["mother_occupation"]
		father_occupation = self.request.POST["father_occupation"]
		annual_family_income = self.request.POST["annual_family_income"]
		caste = self.request.POST["caste"]
		address1 = self.request.POST["address1"]
		address2 = self.request.POST["address2"]
		zipcode = self.request.POST["zipcode"]
		started_on = _convert_string_to_date(self.request.POST["started_on"])
		# logging.info(form_items)

		bioData = BioData(
			rgukt_id = rgukt_id, 
			first_name = first_name, 
			middle_name = middle_name, 
			last_name = last_name, 
			mobile = mobile, 
			email = email, 
			skype = skype, 
			school_name = school_name, 
			class_rank = class_rank, 
			cgpa = cgpa, 
			father_name = father_name, 
			occupation = occupation, 
			annual_income = annual_income, 
			mother_name = mother_name, 
			annual_family_income = annual_family_income, 
			caste = caste, 
			address1 = address1, 
			address2 = address2, 
			zipcode = zipcode, 
			started_on = started_on 
		)
		# for item in form_items:
		# 	setattr(bioData, item[0], item[1])
		bioData.put()
		self.response.out.write(["Form submission successfull with these values", bioData])

class MainHandler(webapp2.RequestHandler):
	def get(self):
		template = JINJA_ENVIRONMENT.get_template('form.html')
		logging.info(template)
		self.response.out.write(template.render({'datetime':datetime.datetime.now()}))
	def post(self):
		form_items = self.request.POST.items()
		started_on = _convert_string_to_date(self.request.POST["started_on"])
		logging.info(form_items)
		bioData = BioData()
		for item in form_items:
			if item[0] == "started_on":
				setattr(bioData, item[0], started_on)
			else:
				setattr(bioData, item[0], item[1])
		bioData.put()
		logging.info(bioData)
		self.response.out.write(["Form submission successfull with these values", bioData])

class BioDataHandler(webapp2.RequestHandler):
	def get(self):
		user = users.get_current_user()
		if not user:
			self.redirect(users.create_login_url(self.request.uri), permanent=True, abort=True, code=302)
		if user.email().lower() not in admins:
			login_url = users.create_logout_url(self.request.uri)
			greeting = 'You are not authorized. <a href="{}">Sign in</a> with different account'.format(login_url)
			self.response.write('<html><body>{}</body></html>'.format(greeting))
		else:

			#to download attendance for each student date as column and penalties as tuple
			self.response.headers['Content-Disposition'] = 'attachment; filename=bio_data_'+str(datetime.datetime.today())+'.csv'
			
			self.response.headers['Content-Type'] = 'application/csv'
			# writer = csv.writer(self.response.out)
			# writer.writerow(['foo','foo,bar', 'bar'])   
			fieldnames = [
				"rgukt_id",
				"first_name",
				"middle_name",
				"last_name",
				"mobile",
				"email",
				"skype",
				"school_name",
				"class_rank",
				"cgpa",
				"dob_day",
				"dob_month",
				"dob_year",
				"gender",
				"date_of_graduation",
				"father_name",
				"father_highest_education",
				"father_occupation",
				"father_annual_income",
				"mother_name",
				"mother_highest_education",
				"mother_occupation",
				"mother_annual_income",
				"annual_family_income",
				"caste",
				"address1",
				"address2",
				"zipcode",
				"started_on",
				"submitted_on"
			]
			
			writer = csv.DictWriter(self.response.out, fieldnames=fieldnames)

			writer.writeheader()
			students = BioData.query()
			for student in students:
				logging.info(student.to_dict())
				writer.writerow(student.to_dict())

app = webapp2.WSGIApplication([
	('/', MainHandler),
	('/download_biodata', BioDataHandler)
], debug=True)
