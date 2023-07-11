# Generated by Django 4.2.2 on 2023-07-10 21:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animaladoptreadycreate',
            name='animal_name',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
        migrations.AlterField(
            model_name='animaladoptreadycreate',
            name='animal_type',
            field=models.CharField(choices=[('dog', 'Dog'), ('cat', 'Cat'), ('other', 'Other')], max_length=30),
        ),
        migrations.AlterField(
            model_name='animaladoptreadycreate',
            name='location',
            field=models.CharField(max_length=40, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
        migrations.AlterField(
            model_name='animalatvetclinic',
            name='name_animal',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
        migrations.AlterField(
            model_name='animalatvetclinic',
            name='type_animal',
            field=models.CharField(choices=[('dog', 'Dog'), ('cat', 'Cat'), ('other', 'Other')], max_length=20),
        ),
        migrations.AlterField(
            model_name='animalatvetclinic',
            name='vetclinic',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
        migrations.AlterField(
            model_name='animalatvetclinic',
            name='vetclinic_city',
            field=models.CharField(max_length=40, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
    ]