# Generated by Django 4.2.2 on 2023-08-08 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adoptionhomemodel',
            name='animal_type',
            field=models.CharField(choices=[('cat', 'Cat'), ('dog', 'Dog'), ('other', 'Other')], max_length=30),
        ),
    ]
