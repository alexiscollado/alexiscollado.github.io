# Generated by Django 2.0.2 on 2018-04-30 15:01

import any_urlfield.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_body',
            field=any_urlfield.models.fields.AnyUrlField(max_length=300, verbose_name='URL'),
        ),
    ]
