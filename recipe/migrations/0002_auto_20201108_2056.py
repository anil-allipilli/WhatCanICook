# Generated by Django 3.1.3 on 2020-11-08 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='group',
            field=models.CharField(max_length=32),
        ),
    ]