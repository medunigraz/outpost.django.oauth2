from django.core.validators import URLValidator
from django.db import models
from django.contrib.auth.models import Group
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

    def is_usable(self, request):
        if not self.groups.exists():
            return True
        return self.groups.intersection(self.user.groups.all()).exists()
