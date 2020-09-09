from django.db import models
from django.contrib.auth.models import User
from cities_light.models import City, Country, Region
from phone_field import PhoneField


class Industry(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return '%s' % (self.name)


class Skill(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return '%s' % (self.name)


class Savedjob(models.Model):
    title = models.TextField()
    url = models.URLField()
    company = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.title


class Profile(models.Model):
    SEX = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    # state = models.ForeignKey(Region, on_delete=models.CASCADE)
    zipcode = models.CharField(max_length=50)
    # country = models.ForeignKey(Country, on_delete=models.CASCADE)
    gender = models.CharField(
        max_length=1, choices=SEX, blank=False, default="")
    skills = models.ManyToManyField(Skill)
    industries = models.ManyToManyField(Industry)
    savedjobs = models.ManyToManyField(Savedjob)
    searchquery = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


# class Currentskill(models.Model):
#     profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     skill = models.ForeignKey(Skill, on_delete=models.CASCADE)


# class Desiredskill(models.Model):
#     profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     skill = models.ForeignKey(Skill, on_delete=models.CASCADE)


# class Currentindustry(models.Model):
#     profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     industry = models.ForeignKey(Skill, on_delete=models.CASCADE)


# class Desiredindustry(models.Model):
#     profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     industry = models.ForeignKey(Skill, on_delete=models.CASCADE)
