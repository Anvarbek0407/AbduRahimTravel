# Generated by Django 4.0.6 on 2022-12-12 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='citytown',
            name='address_iframe',
            field=models.TextField(null=True),
        ),
    ]
