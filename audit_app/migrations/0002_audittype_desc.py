# Generated by Django 2.2 on 2020-03-31 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='audittype',
            name='desc',
            field=models.TextField(blank=True),
        ),
    ]
