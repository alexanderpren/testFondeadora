from django.db import models
ARRAY_KEYS = []
VERSION = 0
from key.controller import CustomValidation
from django.utils.translation import gettext_lazy as _
from rest_framework import status



class Record():
    
    def __init__(self, key_id, value):
        self.record = ""        
        self.key_id = key_id
        self.new_value = value
        self.check_new_value()
    
    def check_new_value(self):
        if self.new_value:
            if(len(ARRAY_KEYS)) == 0:
                self.record = self.create_new_record()
                return self.record
            else:
                if not self.check_repeated_values():
                    self.record = self.create_new_record()
                    return self.record
        
        else:
            raise CustomValidation(
                _("Debe proporcionar campo de Valor"),
                "Keys",
                status.HTTP_400_BAD_REQUEST,
            )
    def create_new_record(self):
        self.increment_version()
        new_record = {"key": self.key_id, "value": self.new_value, "version": VERSION }
        ARRAY_KEYS.append(new_record)
        return new_record
    
   
    def increment_version(self):
        global  VERSION        
        VERSION += 1
        
    
    def check_repeated_values(self):
        repeated_value = False
        for current_index in ARRAY_KEYS:
            if current_index['value'] == self.new_value:
                self.increment_version()
                current_index['version'] = VERSION
                self.record = current_index
                repeated_value = True
                return repeated_value
        return repeated_value

    
        
    