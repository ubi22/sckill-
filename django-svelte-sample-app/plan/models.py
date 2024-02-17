from django.db import models
from user.models import User

class TrainingCours(models.Model):
    name = models.CharField('Название',  max_length=63 )
    desc = models.CharField('Описание', max_length=511)
    students = models.ManyToManyField(User)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='training_courses')
    def __str__(self) :
        return f'{self.name}'
        

class Lesson(models.Model):
    title = models.CharField('Заглавие', max_length = 63)
    text = models.CharField('Текст курса', max_length = 1023)
    cours = models.ForeignKey(TrainingCours, on_delete = models.DO_NOTHING)
    file = models.FileField(upload_to='filess')