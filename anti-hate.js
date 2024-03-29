function checkSentient() {
  // Don't follow the link
  var btn = event.target || event.srcElement;
  event.preventDefault;
  let e = event;
  var inputs = document.getElementsByClassName("sentient-check");
  for (var i = 0; i < inputs.length; i++) {
    var input = inputs.item(i);
    var text = input.value;
    // Open a new connection, using the GET request on the URL endpoint
    const request = async () => {
      const response = await fetch(
        "https://mattboote3324.pythonanywhere.com/sentiment?data=" +
          encodeURI(text)
      );
      const json = await response.json();

      if (!handleFormEvent(json, input)) {
        //Stopping all events from happening.
        e.cancel = true;
        e.returnValue = false;
        e.cancelBubble = true;
        if (e.stopPropagation) e.stopPropagation();
        if (e.preventDefault) e.preventDefault();

        input.focus();
        input.setAttribute("style", "border-color: red;");
        console.log(
          "Sentiment Score too low on input " +
            input.id +
            " - Killing all submit and onclick events"
        );

        return false;
      } else {
        console.log(
          "Sentiment Score is okay on input " +
            input.id +
            ".. Continuing events"
        );
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
