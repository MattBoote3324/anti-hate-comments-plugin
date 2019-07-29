function checkSentient(buttonClicked) {
  // Don't follow the link
  event.preventDefault();
  var inputID = buttonClicked.dataset.input;

  var text = document.getElementById(inputID).value;

  var request = new XMLHttpRequest();

  $.ajax({
    url: "https://mattboote3324.pythonanywhere.com/sentiment",
    type: "post",
    dataType: "json",
    contentType: "application/json",
    success: function(data) {
      var data = JSON.parse(this.response);

      if (request.status >= 200 && request.status < 400) {
        console.log(data.score, data.magnitude);
      } else {
        console.log("error");
      }
    },
    data: {
      text: text
    }
  });
}
