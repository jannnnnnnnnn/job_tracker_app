from django.contrib import admin
from .models import Profile, Skill, Industry, Currentskill, Desiredskill
# Register your models here.

admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Industry)
admin.site.register(Currentskill)
admin.site.register(Desiredskill)
