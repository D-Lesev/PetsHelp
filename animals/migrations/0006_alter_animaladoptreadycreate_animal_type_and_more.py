# Generated by Django 4.2.2 on 2023-07-05 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0005_animaladoptsend_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animaladoptreadycreate',
            name='animal_type',
            field=models.CharField(choices=[('dog', 'Dog'), ('cat', 'Cat'), ('other', 'Other')], max_length=30),
        ),
        migrations.DeleteModel(
            name='AnimalAdoptSend',
        ),
    ]