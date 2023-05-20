"""A Python Flask REST API BoilerPlate (CRUD) Style"""

import argparse
import os
from flask import Flask, jsonify, make_response, session
from flask_cors import CORS
from modules.contacts.contact import CONTACT_REQUEST

APP = Flask(__name__)

### swagger specific ###
APP.register_blueprint(CONTACT_REQUEST, url_prefix='/api/contact')


if __name__ == '__main__':

    PORT = int(os.environ.get('PORT', 5000))
    CORS = CORS(APP, resources={r"/*": {'origins':"*"}})

    APP.run(host='0.0.0.0', port=PORT, debug=True)