from django.urls import path, include
from rest_framework import routers
from key import views

""" key_options = views.KeyViewSet.as_view({
	'put':'put',
	'post':'create'
}) """

urlpatterns = [
   	path('keys/', views.KeyViewSet.as_view({'put': 'put'}), name='keys_api'),
    		

]
