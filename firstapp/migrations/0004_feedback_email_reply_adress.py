# Generated by Django 3.0.4 on 2020-04-25 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_auto_20200425_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='email_reply_adress',
            field=models.ManyToManyField(blank=True, null=True, to='firstapp.Profile'),
        ),
    ]
