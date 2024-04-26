from django.contrib.auth.models import Group
from django.core.validators import URLValidator
from django.db import models
from oauth2_provider.models import AbstractApplication


class Application(AbstractApplication):
    logo = models.ImageField()
    agree = models.BooleanField()
    website = models.TextField(validators=[URLValidator()])
    privacy = models.TextField(validators=[URLValidator()])
    description = models.TextField()
    groups = models.ManyToManyField(Group, blank=True)

    class Meta(AbstractApplication.Meta):
        pass
