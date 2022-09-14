window.onload = function () {

	var seconds = 00;
	var tens = 00;
	var appendTens = document.getElementById("tens");
	var appendSeconds = document.getElementById("seconds");
	var startButt = document.getElementById("start-button");
	var stopButt = document.getElementById("stop-button");
	var resetButt = document.getElementById("reset-button");
	var Interval;

	startButt.onclick = function() {
		clearInterval(Interval);
		Interval = setInterval(startTimer, 10);
		
		}

		stopButt.onclick = function() {
			clearInterval(Interval);
		}

		resetButt.onclick = function() {
			clearInterval(Interval);
			tens = "00";
			seconds = "00";
			appendTens.innerHTML = tens;
			appendSeconds.innerHTML = seconds;
		}

		function startTimer () {
			tens++;

			if(tens <= 9){
				appendTens.innerHTML = "0" + tens;
			}

			if(tens > 9){
				appendTens.innerHTML = tens;

			}

			if (tens > 99) {
				console.log("seconds");
				seconds++;
				appendSeconds.innerHTML = "0" + seconds;
				tens = 0;
				appendTens.innerHTML = "0" + 0;
			}

			if (seconds > 9){
				appendSeconds.innerHTML = seconds;
			}
		}


}