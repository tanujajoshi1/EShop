
from django.contrib import admin
from django.urls import path
from .import views
from .views import *


urlpatterns = [
   path('',Index.as_view()),
   path('signUp',views.signUp),
   path('signIn',Login.as_view())
    
]
