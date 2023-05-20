"""A Python Flask REST API BoilerPlate (CRUD) Style"""

import argparse
import os
from flask import Flask, jsonify, make_response, session
from flask_cors import CORS
from modules.contacts.contact import CONTACT_REQUEST

APP = Flask(__name__)  # Crée une instance de l'application Flask
CORS(APP, origins="*")

### swagger specific ###
APP.register_blueprint(CONTACT_REQUEST, url_prefix='/api/contact')  # Enregistre le blueprint CONTACT_REQUEST pour les routes relatives aux contacts

if __name__ == '__main__':

    PORT = int(os.environ.get('PORT', 5000))  # Récupère le numéro de port à partir de la variable d'environnement PORT ou utilise le port 5000 par défaut
    CORS = CORS(APP, resources={r"/*": {'origins':"*", 'methods': '*'}})  # Active le Cross-Origin Resource Sharing (CORS) pour toutes les ressources et origines

    APP.run(host='0.0.0.0', port=PORT, debug=True)  # Lance l'application Flask en écoutant sur l'adresse IP '0.0.0.0' et le port spécifié, avec le mode de débogage activé
