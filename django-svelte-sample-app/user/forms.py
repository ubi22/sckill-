from django.contrib.auth.forms import UserCreationForm
from .managers import UserManager
from .models import *
from django.urls import reverse_lazy

class RegForm(UserCreationForm):
    class Meta:
        model = User
        success_url = reverse_lazy("myapp:spa")
        fields = ['email', 'username']