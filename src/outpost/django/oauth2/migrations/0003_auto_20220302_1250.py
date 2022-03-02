# Generated by Django 2.2.25 on 2022-03-02 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('oauth2', '0002_auto_20171106_0910'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='groups',
            field=models.ManyToManyField(blank=True, to='auth.Group'),
        ),
        migrations.AlterField(
            model_name='application',
            name='redirect_uris',
            field=models.TextField(blank=True, help_text='Allowed URIs list, space separated'),
        ),
    ]
