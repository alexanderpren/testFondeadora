from django.urls import path, include
from rest_framework import routers
from key import views


key_options = views.KeyViewSet.as_view({
	'put':'put',
	'get':'get'
}) 

urlpatterns = [
   	path('keys/', key_options, name='keys_api'),
    path('keys/<str:string>/', views.GetKeyViewSet.as_view({'get':'get'}), name='get_by_key'),
]
