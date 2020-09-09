from django.forms import ModelForm
from .models import Skill, Industry, Savedjob
from django.contrib.auth.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'


class IndustryForm(ModelForm):
    class Meta:
        model = Industry
        fields = '__all__'


class SavedjobForm(ModelForm):
    class Meta:
        model = Savedjob
        fields = '__all__'
