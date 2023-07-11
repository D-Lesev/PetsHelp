# Generated by Django 4.2.2 on 2023-07-11 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0003_alter_animaladoptreadycreate_animal_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animaladoptreadycreate',
            name='animal_type',
            field=models.CharField(choices=[('dog', 'Dog'), ('cat', 'Cat'), ('other', 'Other')], max_length=30),
        ),
        migrations.AlterField(
            model_name='animalatvetclinic',
            name='type_animal',
            field=models.CharField(choices=[('dog', 'Dog'), ('cat', 'Cat'), ('other', 'Other')], max_length=20),
        ),
    ]
