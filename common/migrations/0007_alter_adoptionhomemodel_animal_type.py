# Generated by Django 4.2.2 on 2023-07-04 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_alter_adoptionhomemodel_animal_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adoptionhomemodel',
            name='animal_type',
            field=models.CharField(choices=[('dog', 'Dog'), ('other', 'Other'), ('cat', 'Cat')], max_length=30),
        ),
    ]
