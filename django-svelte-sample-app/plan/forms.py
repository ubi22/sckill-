from django import forms
from .models import *

class TrainingCourseForm(forms.Form):
    class Meta:
        model = TrainingCours
        fields = ('name', 'desc')

class LessonForm(forms.Form):
    class Meta:
        model = Lesson
        fields = ('title', 'text', 'file')