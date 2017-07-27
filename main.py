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
	sub_caste = ndb.StringProperty()
	houseno = ndb.StringProperty()
	streetname = ndb.StringProperty()
	address1 = ndb.StringProperty()
	district = ndb.StringProperty()
	zipcode = ndb.StringProperty()
	city = ndb.StringProperty()
	started_on = ndb.DateTimeProperty()
	date_of_graduation = ndb.StringProperty()
	dob_day = ndb.StringProperty()
	dob_month = ndb.StringProperty()
	dob_year = ndb.StringProperty()
	father_highest_education = ndb.StringProperty()
	father_occupation = ndb.StringProperty()
	gender = ndb.StringProperty()
	mother_highest_education = ndb.StringProperty()
	mother_occupation = ndb.StringProperty()
	submitted_on = ndb.DateTimeProperty(auto_now=True)
	school_town = ndb.StringProperty()
	school_mandal = ndb.StringProperty()
	school_district = ndb.StringProperty()

class BioDataTime(ndb.Model):
	email = ndb.StringProperty()
	rgukt_id_time = ndb.FloatProperty()
	first_name_time = ndb.FloatProperty()
	middle_name_time = ndb.FloatProperty()
	last_name_time = ndb.FloatProperty()
	mobile_time = ndb.FloatProperty()
	email_time = ndb.FloatProperty()
	skype_time = ndb.FloatProperty()
	school_name_time = ndb.FloatProperty()
	class_rank_time = ndb.FloatProperty()
	cgpa_time = ndb.FloatProperty()
	father_name_time = ndb.FloatProperty()
	mother_name_time = ndb.FloatProperty()
	annual_family_income_time = ndb.FloatProperty()
	caste_time = ndb.FloatProperty()
	address1_time = ndb.FloatProperty()
	address2_time = ndb.FloatProperty()
	zipcode_time = ndb.FloatProperty()
	city_time = ndb.FloatProperty()
	date_of_graduation_time = ndb.FloatProperty()
	dob_day_time = ndb.FloatProperty()
	dob_month_time = ndb.FloatProperty()
	dob_year_time = ndb.FloatProperty()
	father_highest_education_time = ndb.FloatProperty()
	father_occupation_time = ndb.FloatProperty()
	gender_time = ndb.FloatProperty()
	mother_highest_education_time = ndb.FloatProperty()
	mother_occupation_time = ndb.FloatProperty()

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
		sub_caste = self.request.POST["sub_caste"]
		house_no = self.request.POST["houseno"]
		street_name = self.request.POST["streetname"]
		address1 = self.request.POST["address1"]
		address2 = self.request.POST["address2"]
		zipcode = self.request.POST["zipcode"]
		started_on = _convert_string_to_date(self.request.POST["started_on"])
		# logging.info(form_items)
		logging.info("there")
		logging.info(house_no)
		logging.info(street_name)
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
			house_no = house_no,
			street_name = street_name,
			address1 = address1, 
			zipcode = zipcode, 
			started_on = started_on,
			sub_caste = sub_caste			
		)
		logging.info("here")
		logging.info(bioData)
		# for item in form_items:
		# 	setattr(bioData, item[0], item[1])
		bioData.put()

		self.response.out.write(["Form submission successfull with these values", bioData])

class Testing(webapp2.RequestHandler):
	def get(self):
		bioData = BioData()
		setattr(bioData, "rgukt_id_time", "12:23")
		bioData.put()
		return bioData

class MainHandler(webapp2.RequestHandler):
	def get(self):
		template = JINJA_ENVIRONMENT.get_template('form.html')
		logging.info(template)
		self.response.out.write(template.render({'datetime':datetime.datetime.now()}))
	def post(self):
		form_items = self.request.POST.items()
		email = self.request.POST["email"]
		# exist = BioData.query(BioData.email == email).fetch()
		exist = False
		if not exist:
			started_on = _convert_string_to_date(self.request.POST["started_on"])
			logging.info(form_items)
			bioData = BioData()
			bioDataTime = BioDataTime()
			for item in form_items:
				if item[0] == "started_on":
					setattr(bioData, item[0], started_on)
				else:
					if item[0].endswith("_time"):
						setattr(bioDataTime, item[0], float(item[1]))
					else:
						setattr(bioData, item[0], item[1])
			bioData.put()
			setattr(bioDataTime, "email", email)
			bioDataTime.put()
			logging.info(bioData)
			logging.info(bioDataTime)
			# self.response.out.write(["Form submission successfull with these values", bioData])
			self.response.out.write("<html><body><strong>Your data saved successfully</strong></body></html>")
		else:
			self.response.out.write("<html><body><strong>An entry already exists</strong></body></html>")


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
				"cgpa",
				"dob_day",
				"dob_month",
				"dob_year",
				"gender",
				"date_of_graduation",
				"father_name",
				"father_highest_education",
				"father_occupation",
				"mother_name",
				"mother_highest_education",
				"mother_occupation",
				"annual_family_income",
				"caste",
				"sub_caste",
				"houseno",
				"streetname",
				"address1",
				"district",
				"zipcode",
				"city",
				"response_time",
				"school_district",
				'school_mandal', 
				'school_town',
				'address2',
				'class_rank'
			]
			
			writer = csv.DictWriter(self.response.out, fieldnames=fieldnames)

			writer.writeheader()
			students = BioData.query()
			for student in students:
				student = student.to_dict()
				if student["started_on"]:
					timeDiff = student["submitted_on"] - student["started_on"]
					student["response_time"] = round(timeDiff.total_seconds() / 60)
				student.pop("started_on", None)
				student.pop("submitted_on", None)
				writer.writerow(student)

class BioDataTimeHandler(webapp2.RequestHandler):
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
			self.response.headers['Content-Disposition'] = 'attachment; filename=bio_data_timestamp_'+str(datetime.datetime.today())+'.csv'
			
			self.response.headers['Content-Type'] = 'application/csv'
			# writer = csv.writer(self.response.out)
			# writer.writerow(['foo','foo,bar', 'bar'])   
			fieldnames = [
				"email",
				"rgukt_id_time",
				"first_name_time",
				"middle_name_time",
				"last_name_time",
				"mobile_time",
				"email_time",
				"skype_time",
				"school_name_time",
				"class_rank_time",
				"cgpa_time",
				"dob_day_time",
				"dob_month_time",
				"dob_year_time",
				"gender_time",
				"date_of_graduation_time",
				"father_name_time",
				"father_highest_education_time",
				"father_occupation_time",
				"mother_name_time",
				"mother_highest_education_time",
				"mother_occupation_time",
				"annual_family_income_time",
				"caste_time",
				"address1_time",
				"address2_time",
				"zipcode_time",
				"city_time",
				"total_response_time"
			]
			
			writer = csv.DictWriter(self.response.out, fieldnames=fieldnames)

			writer.writeheader()
			students = BioDataTime.query()
			for student in students:
				student = student.to_dict()
				total = 0
				for item in student:
					if item in ["email", "total_response_time"]:
						continue
					if student[item]:
						time = round(student[item] / 1000)
						student[item] = time
						total += time
				student['total_response_time'] = total
				writer.writerow(student)


app = webapp2.WSGIApplication([
	('/', MainHandler),
	('/testing', Testing),
	('/download_biodata', BioDataHandler),
	('/download_biodata_timestamp', BioDataTimeHandler)
], debug=True)
