function checkSentient(buttonClicked) {
  // Don't follow the link
  event.preventDefault();
  var inputID = buttonClicked.dataset.input;

  var text = document.getElementById(inputID).value;

  var request = new XMLHttpRequest();

  // Open a new connection, using the GET request on the URL endpoint
  request.open(
    "POST",
    "https://mattboote3324.pythonanywhere.com/sentiment",
    true
  );
  request.onload = function() {
    // Begin accessing JSON data here
    var data = JSON.parse(this.response);

    if (request.status >= 200 && request.status < 400) {
      console.log(data.score, data.magnitude);
    } else {
      console.log("error");
    }
  };

  request.send({ text: text });
}
