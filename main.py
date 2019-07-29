

# [START gae_flex_quickstart]
import logging

from flask import Flask, send_from_directory, make_response
from flask import request
from flask import Response
import json
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import os
from google.oauth2 import service_account

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/mattboote3324/anti-hate/sentiment-analyis-be936a883ba2.json"

app = Flask(__name__)


@app.route('/sentiment', methods=['POST'])
def hello():
    """Return a friendly HTTP greeting."""
    resp = make_response(sentiment_checker(request))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


def sentiment_checker(request):
    # Instantiates a client
    client = language.LanguageServiceClient()

    # This is our request data coming in
    data = json.loads(request.data)
    text = data['text']

    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment

    result = '"score": "{}", "magnitude": "{}"'.format(
        sentiment.score, sentiment.magnitude)
    jsonResp = '{' + result + '}'
    return jsonResp


@app.route('/anti-hate', methods=['GET'])
def send_script():
    resp = make_response(send_from_directory(
        '/home/mattboote3324/anti-hate/', 'anti-hate.js'))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_flex_quickstart]
