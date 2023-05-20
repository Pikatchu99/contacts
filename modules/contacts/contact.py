from user_agents import parse
from flask import Blueprint, request
import jwt, json
from ..utils import *
from .contactInterface import ContactInterface


CONTACT_REQUEST = Blueprint('contact', __name__)

@CONTACT_REQUEST.route('/create', methods=['POST'])
def create():
    try:
        datas = request.get_json(force=True)
        contact = ContactInterface(datas)
        contact_created = contact.create()
        return success_response(code=201, data=contact_created)
    except Exception as error:
        return error_response(message=str(error), code=500)


@CONTACT_REQUEST.route('/update', methods=['PUT'])
def update():
    try:
        datas = request.get_json(force=True)

        contact = ContactInterface(datas)
        contact_to_update = contact.update(
            {"id": datas['id']},
            datas['datas']
        )
        return success_response(code=200)
    except Exception as error:
        return error_response(message=str(error), code=500)


@CONTACT_REQUEST.route('/delete', methods=['DELETE'])
def delete():
    try:
        datas = request.get_json(force=True)

        contact = ContactInterface(datas)
        contact_to_delete = contact.delete({"id": datas['id']})
        return success_response(code=200)
    except Exception as error:
        return error_response(message=str(error), code=500)

@CONTACT_REQUEST.route('/get', methods=['GET'])
def get_contact():
    try:
        datas = request.args.to_dict()

        contact = ContactInterface(datas)

        contact = contact.get_contact({"id": datas['id']})
        return success_response(code=200, data=contact)
    except Exception as error:
        return error_response(message=str(error), code=500)

@CONTACT_REQUEST.route('/get/all', methods=['GET'])
def get_contact_all():
    try:
        contact = ContactInterface({})
        contacts = contact.get_all_contacts()
        return success_response(code=200, data=contacts)
    except Exception as error:
        return error_response(message=str(error), code=500)