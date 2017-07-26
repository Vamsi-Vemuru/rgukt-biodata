var last, diff, current;
document.addEventListener('focusin', function (e) {
	current = e.target.name;
	// console.log(current);
	if ( last ) {
		diff = event.timeStamp - last;
		console.log([current, diff])
	} else {
		console.log([current])
	}
	last = event.timeStamp;
    // console.log('focusin !', e.target.name);
    // console.log('focusin !', e.timeStamp);
    // var start = new Date();
	// console.log("START: " + start);
	// setTimeout(function() {
	//   console.log("FINISH: " + new Date())
	//   console.log("ELAPSED MS: " + (new Date() -start) + "ms")
	//   console.log("ELAPSED MIN: " + ((new Date()-start)/1000/60) + " min")
	// }, 100);
})

document.addEventListener('focusout', function(e){
	// console.log(current);
	current = e.target.name;
	console.log(["out", current]);
	
})