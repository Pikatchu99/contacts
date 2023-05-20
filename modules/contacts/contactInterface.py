import bcrypt
from ..utils import get_env_value
from pymongo import MongoClient
from bson.objectid import ObjectId

class ContactInterface:
    def __init__(self):
        self.connexion = MongoClient(get_env_value('DATABASE_URL'))  # Initialise la connexion à la base de données MongoDB
        self.db = self.connexion['contacts+']  # Sélectionne la base de données 'contacts+'
        self.contacts = self.db['contacts']  # Sélectionne la collection 'contacts'

    def init_contact(self, datas):
        self.fullname = datas.get('fullname', "default")  # Initialise le nom complet du contact avec la valeur de 'fullname' dans les données ou "default" si non spécifié
        self.email = datas.get('email', "default@exemple.com")  # Initialise l'e-mail du contact avec la valeur de 'email' dans les données ou "default@exemple.com" si non spécifié
        self.contact = datas['contact']  # Initialise les informations de contact du contact avec la valeur de 'contact' dans les données

    def create(self):
        new_contact = {
            "id": str(ObjectId()),  # Génère un nouvel identifiant unique pour le contact
            "fullname": self.fullname,  # Nom complet du contact
            "email": self.email,  # E-mail du contact
            "contact": self.contact  # Informations de contact du contact
        }
        self.contacts.insert_one(new_contact)  # Insère le nouveau contact dans la collection 'contacts'
        del new_contact['_id']  # Supprime le champ '_id' qui n'est pas nécessaire à retourner
        return new_contact  # Retourne le nouveau contact créé

    def update(self, filter, datas):
        self.contacts.update_one(filter, {'$set': datas})  # Met à jour le contact correspondant au filtre avec les nouvelles données spécifiées

    def delete(self, filter):
        self.contacts.delete_one(filter)  # Supprime le contact correspondant au filtre de la collection 'contacts'

    def get_contact(self, filter):
        contact = self.contacts.find_one(filter)  # Récupère le contact correspondant au filtre de la collection 'contacts'
        del contact['_id']  # Supprime le champ '_id' qui n'est pas nécessaire à retourner
        return contact  # Retourne le contact récupéré

    def get_all_contacts(self):
        contacts = list(self.contacts.find({}))  # Récupère tous les contacts de la collection 'contacts' et les convertit en une liste
        for contact in contacts:
            if '_id' in contact:
                del contact['_id']  # Supprime le champ '_id' de chaque contact qui n'est pas nécessaire à retourner
        return contacts  # Retourne tous les contacts récupérés
