from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets, permissions



# Create your views here.

class KeyViewSet(viewsets.ViewSet):
    
    
    def put(self, request):
        from key.models import  Record
        from key.controller  import get_name_key
        
        key_id = get_name_key(request.data)      
        new_record = Record(key_id,request.data[key_id])       
        return Response(new_record.record)

    def get(self, request):
        from key.controller  import get_name_key, is_key_valid,get_record_by_key, get_record_by_key_and_version      
        key_id = get_name_key(request.data)
        
        
        is_current_record = is_key_valid(key_id)
        if is_current_record:
            if(request.data[key_id]):
                current_record = get_record_by_key_and_version(key_id, request.data[key_id])
            else:
                 current_record = get_record_by_key(key_id)
        return Response(current_record)
                
            
                
          


class GetKeyViewSet(viewsets.ViewSet):
     def get(self, request, string):
        print("Hola")
    
    





