from django.urls import path
from .views import *

app_name='user'

urlpatterns = [
    path('registration/', RegisterView.as_view())
]
