from django.forms import ModelForm
from .models import *


class Form(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
