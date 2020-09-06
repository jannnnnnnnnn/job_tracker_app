from django.db import models
from django.contrib.auth.models import User
# from django_countries.fields import CountryField
from cities_light.models import City, Country, Region


# class Industry(models.Model):
#     industries = models.CharField(max_length=200)

#     def __str__(self):
#         return '%s' % (self.industries)


# class Skill(models.Model):
#     skills = models.CharField(max_length=200)

#     def __str__(self):
#         return '%s' % (self.skills)


class Profile(models.Model):
    SEX = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField()
    address = models.CharField(max_length=50, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    state = models.ForeignKey(Region, on_delete=models.CASCADE)
    zipcode = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    # # gender = models.CharField(
    #     max_length=1, choices=SEX, blank=False, default="")
    # current_skills = models.ManyToManyField(Skill)
    # current_industry = models.ManyToManyField(Industry)
    # desired_skills = models.ManyToManyField(Skill)
    # desired_industry = models.ManyToManyField(Industry)
