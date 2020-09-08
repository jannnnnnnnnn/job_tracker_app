from django.forms import ModelForm
from .models import Skill, Industry, Savedjob


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
