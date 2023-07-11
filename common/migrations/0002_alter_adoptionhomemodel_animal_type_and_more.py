# Generated by Django 4.2.2 on 2023-07-10 21:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adoptionhomemodel',
            name='animal_type',
            field=models.CharField(choices=[('dog', 'Dog'), ('cat', 'Cat'), ('other', 'Other')], max_length=30),
        ),
        migrations.AlterField(
            model_name='adoptionhomemodel',
            name='city',
            field=models.CharField(max_length=25, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
        migrations.AlterField(
            model_name='adoptionhomemodel',
            name='province',
            field=models.CharField(max_length=25, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
        migrations.AlterField(
            model_name='adoptionhomemodel',
            name='title',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
        migrations.AlterField(
            model_name='adoptpetmodel',
            name='name_pet',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
        migrations.AlterField(
            model_name='shareanimalmodel',
            name='city',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
        migrations.AlterField(
            model_name='shareanimalmodel',
            name='province',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
        migrations.AlterField(
            model_name='shareanimalmodel',
            name='title',
            field=models.CharField(max_length=40, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
    ]