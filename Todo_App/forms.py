from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Task
from django.forms import ModelForm

class register(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

class tasks(ModelForm):
    class Meta:
        model = Task
        fields = ['user','title','description','complete']
