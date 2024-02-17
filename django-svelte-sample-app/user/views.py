from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from user.forms import *

class RegisterView(FormView):
    form_class = RegForm
    success_url = reverse_lazy("spa")
    template_name = 'registration.html'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)