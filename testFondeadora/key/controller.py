from key.models import ARRAY_KEYS
from rest_framework.exceptions import APIException
from rest_framework import status
from django.utils.translation import gettext_lazy as _
from django.utils.encoding import force_text




def is_key_valid(key_id):
    if check_exist_key(key_id):
        return True
    else:
        raise CustomValidation(
                _("No Existe la llave"),
                "Keys",
                status.HTTP_400_BAD_REQUEST,
            )


def check_exist_key(key):
    find_item = False
    for current_index in ARRAY_KEYS:
            if current_index['key'] == key:              
                find_item = True
                return find_item
    return find_item
            


def get_name_key(new_value):    
    for key, value in new_value.items():
        return key

def get_record_by_key(key_id):
    temp_array = []
    for current_index in ARRAY_KEYS:
        if current_index['key'] == key_id:
            temp_array.append(current_index)
    last_version = sort_array(temp_array)
    return last_version

def get_record_by_key_and_version(key_id):
    temp_array = []
    for current_index in ARRAY_KEYS:
        if current_index['key'] == key_id:
            temp_array.append(current_index)
    last_version = sort_array(temp_array)
    return last_version


def sort_array(current_array):
    new_sort_array = sorted(current_array, key=lambda llave : llave['value'])
    return new_sort_array[len(current_array) -1 ]
    
    
    
    

    
    

class CustomValidation(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = "A server error ocurred"

    def __init__(self, detail, field, status_code=500):
        if status_code is not None:
            self.status_code = status_code
            if detail is not None:
                if detail.__class__.__name__ == 'ValidationError':
                    self.detail = detail.detail
                else:
                    self.detail = {field: force_text(detail)}
            else:
                self.detail = {"detail": force_text(self.default_detail)}
    
    
