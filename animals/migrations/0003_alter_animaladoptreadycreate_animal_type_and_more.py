# Generated by Django 4.2.2 on 2023-07-11 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0002_alter_animaladoptreadycreate_animal_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animaladoptreadycreate',
            name='animal_type',
            field=models.CharField(choices=[('dog', 'Dog'), ('other', 'Other'), ('cat', 'Cat')], max_length=30),
        ),
        migrations.AlterField(
            model_name='animalatvetclinic',
            name='type_animal',
            field=models.CharField(choices=[('dog', 'Dog'), ('other', 'Other'), ('cat', 'Cat')], max_length=20),
        ),
    ]