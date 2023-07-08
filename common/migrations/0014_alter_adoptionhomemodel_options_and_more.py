# Generated by Django 4.2.2 on 2023-07-08 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0013_remove_shareanimalmodel_address_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adoptionhomemodel',
            options={'verbose_name_plural': 'AdoptionHome'},
        ),
        migrations.AlterModelOptions(
            name='adoptpetmodel',
            options={'verbose_name_plural': 'AdoptPet'},
        ),
        migrations.AlterModelOptions(
            name='shareanimalmodel',
            options={'verbose_name_plural': 'ShareAnimal'},
        ),
        migrations.AlterField(
            model_name='adoptionhomemodel',
            name='animal_type',
            field=models.CharField(choices=[('dog', 'Dog'), ('cat', 'Cat'), ('other', 'Other')], max_length=30),
        ),
    ]
