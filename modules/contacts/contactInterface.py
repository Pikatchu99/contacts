import bcrypt
from ..utils import get_env_value
from pymongo import MongoClient
from bson.objectid import ObjectId

class ContactInterface:
    def __init__(self, datas):
        self.fullname = datas.get('fullname', "default")
        self.email = datas.get('email', "default@exemple.com")
        self.contact = datas.get('contact', "default")

        self.connexion = MongoClient(get_env_value('DATABASE_URL'))
        self.db = self.connexion['contacts+']
        self.contacts = self.db['contacts']

    def create(self):
        new_contact = {
            "id": str(ObjectId()),
            "fullname": self.fullname,
            "email": self.email,
            "contact": self.contact
        }
        self.contacts.insert_one(new_contact)
        del new_contact['_id']
        return new_contact

    def update(self, filter, datas):
        self.contacts.update_one(filter, {'$set': datas})

    def delete(self, filter):
        self.contacts.delete_one(filter)

    def get_contact(self, filter):
        contact = self.contacts.find_one(filter)
        del contact['_id']
        return contact

    def get_all_contacts(self):
        contacts = list(self.contacts.find({}))
        print(contacts)
        for contact in contacts:
            if '_id' in contact:
                del contact['_id']
        return contacts