var canvas, context;
var CanvasText = new CanvasText;	
	
window.onload = function(){
	var teendiv = document.getElementById('teenbot');
	teendiv.innerHTML = "<div id='container' style='position:relative;width:800px;height:800px'><canvas id='canvas1' width='400' height='370'></canvas><textarea id='formElement' placeholder='Enter text here' style='position:absolute;left:16px;top:230px;width:350px;height:55px;resize:none;'></textarea></div>"

	canvas = document.getElementById("canvas1");
	context = canvas.getContext("2d");

	var background = new Image();
	background.src = "imwindow.png";
	background.onload = function(){
		context.drawImage(background,0,0);
	}	

	CanvasText.config({
		canvasId: "canvas1",
		fontFamily: "Times new roman",
		fontSize: "14px",
		fontWeight: "normal",
		fontColor: "#000",
		lineHeight: "12"
	});

	CanvasText.defineClass("screenname",{
		fontFamily: "Times new roman",
		fontSize: "14px",
		fontWeight: "bold",
		fontColor: "#0000FF",
		lineHeight: "12"
	});

	CanvasText.defineClass("uscreenname",{
		fontFamily: "Times new roman",
		fontSize: "14px",
		fontWeight: "bold",
		fontColor: "#FF0000",
		lineHeight: "12"
	});

	function doRequest(url, textQuery, callback) {
		var xmlhttp = new XMLHttpRequest(); // create a new request here

		xmlhttp.open("GET", url + "?text=" + encodeURI(textQuery), true); // for async
		xmlhttp.onreadystatechange=function() {	 
			if (xmlhttp.readyState==4) {
				if (xmlhttp.status == 200) {

				// pass the response to the callback function
				callback(null, xmlhttp.responseText);

				} else {
				// pass the error to the callback function
					callback(xmlhttp.statusText);
				}
			}
		}
		xmlhttp.send(null);
	}

	var textarea = document.getElementById('formElement');

		textarea.onkeydown = function (e) {
			var code = (e.keyCode ? e.keyCode : e.which);
			if (code == 13) {
				var textQuery = textarea.value
// replace the URL here with the one where botserver.py is running
				teenText = doRequest('http://your-url-here.com/teenbot', textQuery, function(err, response) { // pass an anonymous function
					if (response) {
						context.clearRect(0, 0, canvas.width, canvas.height);
						context.drawImage(background,0,0);
// You can format this text any way you want.
						var text = "<class='uscreenname'>Me:</class> " + textarea.value + "<br /><class='screenname'>CaptainH: </class>" + response
						textarea.value = "";
						CanvasText.drawText({
							text: text,
							x: 17,
							y: 76,
							boxWidth: 365
						});

					} else {
						alert('Error: ' + err);
					} 
				});
			}
		}
}