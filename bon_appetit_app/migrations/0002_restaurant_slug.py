# Generated by Django 2.1.5 on 2020-03-14 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bon_appetit_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
