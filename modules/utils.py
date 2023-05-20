# Import des packages
import os
from flask import jsonify

# Fonction pour obtenir une valeur d'une variable d'environnement
def get_env_value(key):
    return os.getenv(key, None)

# Fonction pour générer une réponse réussie
def success_response(status=True, message=None, data={}, code=200):
    return jsonify({
        "status": status,
        "message": message,
        "data": data
    }), code

# Fonction pour générer une réponse d'erreur
def error_response(status=False, message=None, data={}, code=400):
    return jsonify({
        "status": status,
        "message": message,
        "data": data
    }), code
