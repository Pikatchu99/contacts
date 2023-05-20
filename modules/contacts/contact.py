from user_agents import parse
from flask import Blueprint, request
import jwt, json
from ..utils import *
from .contactInterface import ContactInterface
from flask_cors import cross_origin


# Création d'un Blueprint pour les requêtes relatives aux contacts
CONTACT_REQUEST = Blueprint('contact', __name__)

# Route pour la création d'un contact
@CONTACT_REQUEST.route('/create', methods=['POST'])
@cross_origin() 
def create():
    try:
        datas = request.get_json(force=True)  # Récupère les données JSON envoyées avec la requête
        contact = ContactInterface()  # Initialise l'interface de contact
        contact.init_contact(datas)  # Initialise le contact avec les données reçues
        contact_created = contact.create()  # Crée le contact dans la base de données
        return success_response(code=201, data=contact_created)  # Retourne une réponse réussie avec le contact créé
    except Exception as error:
        return error_response(message=str(error), code=500)  # Retourne une réponse d'erreur avec le message d'erreur

# Route pour la mise à jour d'un contact
@CONTACT_REQUEST.route('/update', methods=['PUT'])
@cross_origin() 
def update():
    try:
        datas = request.get_json(force=True)  # Récupère les données JSON envoyées avec la requête

        contact = ContactInterface()  # Initialise l'interface de contact
        contact_to_update = contact.update(
            {"id": datas['id']},  # Identifiant du contact à mettre à jour
            datas['datas']  # Nouvelles données du contact
        )
        return success_response(code=200)  # Retourne une réponse réussie
    except Exception as error:
        return error_response(message=str(error), code=500)  # Retourne une réponse d'erreur avec le message d'erreur

# Route pour la suppression d'un contact
@CONTACT_REQUEST.route('/delete', methods=['DELETE'])
@cross_origin() 
def delete():
    try:
        datas = request.get_json(force=True)  # Récupère les données JSON envoyées avec la requête

        contact = ContactInterface()  # Initialise l'interface de contact
        contact_to_delete = contact.delete({"id": datas['id']})  # Supprime le contact de la base de données
        return success_response(code=200)  # Retourne une réponse réussie
    except Exception as error:
        return error_response(message=str(error), code=500)  # Retourne une réponse d'erreur avec le message d'erreur

# Route pour obtenir un contact spécifique
@CONTACT_REQUEST.route('/get', methods=['GET'])
@cross_origin() 
def get_contact():
    try:
        datas = request.args.to_dict()  # Récupère les paramètres de la requête GET

        contact = ContactInterface()  # Initialise l'interface de contact
        contact = contact.get_contact({"id": datas['id']})  # Récupère le contact spécifié par l'identifiant
        return success_response(code=200, data=contact)  # Retourne une réponse réussie avec le contact
    except Exception as error:
        return error_response(message=str(error), code=500)  # Retourne une réponse d'erreur avec le message d'erreur

# Route pour obtenir tous les contacts
@CONTACT_REQUEST.route('/get/all', methods=['GET'])
@cross_origin() 
def get_contact_all():
    try:
        contact = ContactInterface()  # Initialise l'interface de contact sans filtre
        contacts = contact.get_all_contacts()  # Récupère tous les contacts de la base de données
        return success_response(code=200, data=contacts)  # Retourne une réponse réussie avec tous les contacts
    except Exception as error:
        return error_response(message=str(error), code=500)  # Retourne une réponse d'erreur avec le message d'erreur
