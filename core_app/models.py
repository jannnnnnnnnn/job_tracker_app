from django.db import models
from django.contrib.auth.models import User
from cities_light.models import City, Country, Region
from phone_field import PhoneField


class Industry(models.Model):
    industries = models.CharField(max_length=200)

    def __str__(self):
        return '%s' % (self.industries)


class Skill(models.Model):
    skills = models.CharField(max_length=200)

    def __str__(self):
        return '%s' % (self.skills)


class Profile(models.Model):
    SEX = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    address = models.CharField(max_length=50, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    # state = models.ForeignKey(Region, on_delete=models.CASCADE)
    zipcode = models.CharField(max_length=50)
    # country = models.ForeignKey(Country, on_delete=models.CASCADE)
    gender = models.CharField(
        max_length=1, choices=SEX, blank=False, default="")

    def __str__(self):
        return self.user.username


class Currentskill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)


class Desiredskill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)


class Currentindustry(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    industry = models.ForeignKey(Skill, on_delete=models.CASCADE)


class Desiredindustry(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    industry = models.ForeignKey(Skill, on_delete=models.CASCADE)
