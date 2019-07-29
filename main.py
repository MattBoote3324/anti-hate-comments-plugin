from google.oauth2 import service_account  # Google cloud imports
from google.cloud.language import types
from google.cloud.language import enums
from google.cloud import language
from flask_cors import CORS  # Flask related imports
from flask import Response
from flask import request
from flask import Flask, send_from_directory, make_response
import os  # MISC Imports
import json
import logging
_author__ = "Matthew Boote"
__version__ = "1.0.1"
__maintainer__ = "Matthew Boote"
__email__ = "bootematt1@gmail.com"
__status__ = "Production"


# This sets up the credentials to use the Google NL API
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/mattboote3324/anti-hate/sentiment-analyis-be936a883ba2.json"

app = Flask(__name__)
CORS(app)  # Added CORS to ensure there are no cross compatibility issues!

#-------------------------------------Flask route for the sentiment endpoint!-------------------------------------#
@app.route('/sentiment', methods=['GET'])
def hello():
    """Return a friendly HTTP greeting."""
    # Instantiates a client
    client = language.LanguageServiceClient()

    # This is our request data coming in. Currently as a param but could be moved into request body
    text = request.args.get('data')
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment

    # Constructing our repsonse
    result = {}
    result['score'] = sentiment.score
    result['magntitude'] = sentiment.magntitude

    return json.dumps(result)


#-------------------------------------------REQUEST FOR JAVASCRIPT----------------------------------#
@app.route('/anti-hate', methods=['GET'])
def send_script():
    return send_from_directory(
        '/home/mattboote3324/anti-hate/', 'anti-hate.js')

#-----------------------------------------ERROR HANDLING---------------------------------------------#
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
