#Import packages
import os
from flask import jsonify


#Function to get key from env
def get_env_value(key):
    return os.getenv(key, None)

def success_response(status=True, message=None, data={}, code=200):
    return jsonify({
        "status": status,
        "message": message,
        "data": data
    }), code


def error_response(status=False, message=None, data={}, code=400):
    return jsonify({
        "status": status,
        "message": message,
        "data": data
    }), code