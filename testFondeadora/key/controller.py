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
                _("No Existe la llave que desea buscar"),
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
    temp_array = iterate_array(key_id)  
    last_version = get_newest_version_value(temp_array)
    return last_version

def get_record_by_key_and_version(key_id,version):
    
    try:
        int_version = int(version)
    except:
        raise CustomValidation(
                _("Tipo de dato incorrecto para Version"),
                "Keys",
                status.HTTP_400_BAD_REQUEST,
            )
        
    temp_array = iterate_array(key_id) 
    record_by_version = get_desired_version(temp_array,int_version)
    if record_by_version:
        return record_by_version
    else:
        sorted_array = get_sorted_array(temp_array)
        new_record = find_closest_version_smaller(sorted_array, int_version)
        if new_record:
            return new_record
        else:
            raise CustomValidation(
                _("No Existen llaves cercanas a la version # {} ".format(int_version)),
                "Keys",
                status.HTTP_400_BAD_REQUEST,
            )
            

       

def find_closest_version_smaller(array, version):
    tmp_record = None
    for current_index in array:
        if current_index['version'] <= version:
            tmp_record = current_index
    return tmp_record
             
             
    
    

def iterate_array(key_id):
    temp_array = []
    for current_index in ARRAY_KEYS:
        if current_index['key'] == key_id:
            temp_array.append(current_index)
    return temp_array

def get_desired_version(temp_array,version):
    find_record = None
    for current_index in temp_array:
        if current_index['version'] == version:
            find_record = current_index
            
    return find_record


def get_newest_version_value(current_array):
    new_sort_array = sorted(current_array, key=lambda llave : llave['value'])
    return new_sort_array[len(current_array) -1 ]

def get_sorted_array(current_array):
    new_sort_array = sorted(current_array, key=lambda llave : llave['version'])
    return new_sort_array

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
    
    
def get_list():
    new_list = ARRAY_KEYS
