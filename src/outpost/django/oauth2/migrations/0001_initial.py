# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-16 08:53
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import oauth2_provider
import oauth2_provider.generators
import oauth2_provider.validators


if tuple(map(int, oauth2_provider.__version__.split("."))) >= (1, 3, 2):
    RedirectURIValidator = oauth2_provider.validators.RedirectURIValidator
else:
    RedirectURIValidator = oauth2_provider.validators.validate_uris


class Migration(migrations.Migration):

    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name="Application",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "client_id",
                    models.CharField(
                        db_index=True,
                        default=oauth2_provider.generators.generate_client_id,
                        max_length=100,
                        unique=True,
                    ),
                ),
                (
                    "redirect_uris",
                    models.TextField(
                        blank=True,
                        help_text="Allowed URIs list, space separated",
                        validators=[RedirectURIValidator],
                    ),
                ),
                (
                    "client_type",
                    models.CharField(
                        choices=[
                            ("confidential", "Confidential"),
                            ("public", "Public"),
                        ],
                        max_length=32,
                    ),
                ),
                (
                    "authorization_grant_type",
                    models.CharField(
                        choices=[
                            ("authorization-code", "Authorization code"),
                            ("implicit", "Implicit"),
                            ("password", "Resource owner password-based"),
                            ("client-credentials", "Client credentials"),
                        ],
                        max_length=32,
                    ),
                ),
                (
                    "client_secret",
                    models.CharField(
                        blank=True,
                        db_index=True,
                        default=oauth2_provider.generators.generate_client_secret,
                        max_length=255,
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=255)),
                ("skip_authorization", models.BooleanField(default=False)),
                ("logo", models.ImageField(upload_to="")),
                ("agree", models.BooleanField()),
                (
                    "website",
                    models.TextField(
                        validators=[django.core.validators.URLValidator()]
                    ),
                ),
                (
                    "privacy",
                    models.TextField(
                        validators=[django.core.validators.URLValidator()]
                    ),
                ),
                ("description", models.TextField()),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="oauth2_application",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"abstract": False},
        )
    ]
