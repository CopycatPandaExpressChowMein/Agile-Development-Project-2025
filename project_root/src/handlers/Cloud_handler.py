import os 
import firebase_admin
from firebase_admin import credentials, firestore
from PyQt5.QtCore import QDate
from src.handlers.User_entry_object import User_entry

class Cloud_handler:
    
    # Få den absoluta sökvägen till credentials-filen
    __BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Få den aktuella katalogen för denna fil.
    __CREDENTIALS_PATH = os.path.join(__BASE_DIR, "firebase-credentials.json")  # Konstruera den fullständiga sökvägen.
    
    def __init__(self):
        __cred = credentials.Certificate(self.__CREDENTIALS_PATH)  # ✅ Nu kommer den alltid att hitta filen.
        
        firebase_admin.initialize_app(__cred)
        self.db = firestore.client()

    def add_data(self, user_id, entry_id, dictionary):
        db_ref = self.db.collection(user_id).document(entry_id)
        db_ref.set(dictionary)

    def get_data(self, user_id, entry_id):
        user_db_data = self.db.collection(user_id).document(entry_id).get()
        return user_db_data.to_dict()
    
    def add_user_entries(self, user_id, dictionary):
            
        entry_id_list = self.get_data(user_id, "entry_id_list")

        if entry_id_list == None:
            entry_id_list = {}

        for key in dictionary.keys():
            self.add_data(user_id, key.toString(), dictionary.get(key).__dict__)
            entry_id_list[key.toString()] = ""
            
        self.add_data(user_id, "entry_id_list", entry_id_list)

    def get_user_entries(self, user_id):
        temp_dict = {}
        cloud_dict_keys = self.get_data(user_id, "entry_id_list")
        
        for key in cloud_dict_keys:
            temp_entry = self.get_data(user_id, key)

            temp_wellbeing = temp_entry.get("_User_entry__wellbeing")
            temp_anxiety = temp_entry.get("_User_entry__anxiety")
            temp_meals = temp_entry.get("_User_entry__meals")
            temp_connected_boolean = temp_entry.get("_User_entry__connected_boolean")
            temp_rest_boolean = temp_entry.get("_User_entry__rest_boolean")
            temp_exercise_boolean = temp_entry.get("_User_entry__exercise_boolean")
            temp_alcohol_boolean = temp_entry.get("_User_entry__alcohol_boolean")
            temp_drug_boolean = temp_entry.get("_User_entry__drug_boolean")
            temp_notes = temp_entry.get("_User_entry__notes")


            temp_dict[QDate.fromString(key)] = User_entry(temp_wellbeing, temp_anxiety, temp_meals, 
                                                          temp_connected_boolean, temp_rest_boolean, 
                                                          temp_exercise_boolean, temp_alcohol_boolean, 
                                                          temp_drug_boolean, temp_notes)
        
        return temp_dict
