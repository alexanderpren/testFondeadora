from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework import viewsets, permissions

# Create your views here.

class KeyViewSet(viewsets.ViewSet):
    
    
    def put(self, request):
        print("Hola")
    





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