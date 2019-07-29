function checkSentient() {
  // Don't follow the link
  event.preventDefault();
  var btn = event.target || event.srcElement;
  var inputs = document.getElementsByClassName("sentient-check");
  for (var i = 0; i < input.length; i++) {
    var input = slides.item(i);
    var text = input.value;
    // Open a new connection, using the GET request on the URL endpoint
    const request = async () => {
      const response = await fetch(
        "https://mattboote3324.pythonanywhere.com/sentiment?data=" +
          encodeURI(text)
      );
      const json = await response.text();
      console.log(json);
      if (!handleFormEvent(json, input)) {
        //Stopping all events from happening.
        event.cancel = true;
        event.returnValue = false;
        event.cancelBubble = true;
        if (event.stopPropagation) event.stopPropagation();
        if (event.preventDefault) event.preventDefault();

        input.focus();

        return false;
      }
    };

    request();
  }
}

function handleFormEvent(sentimentJSON, input) {
  const NEGATIVE_SENTIENT = -0.5;
  var score = sentimentJSON.score;
  var magnitude = sentimentJSON.magnitude;

  if (score < NEGATIVE_SENTIENT) {
    return false;
  }
  return true;
}
