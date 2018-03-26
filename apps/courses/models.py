# Inside models.py
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 2:
            errors["name"] = "Name should be more than 1 character"
        if len(postData['description']) < 1:
            errors["description"] = "Please enter a description."
        return errors
class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    # age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
