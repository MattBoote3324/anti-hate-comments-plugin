var Sentiment = require("sentiment");

var sentiment = new Sentiment();

$(".anti-hate-check").click(function(event) {
  // Don't follow the link
  event.preventDefault();
  var text = $(".anti-hate-check").value;
  var docx = sentiment.analyze(text);
  // Log the clicked element in the console
  console.log(docx);
});
