# Generated by Django 4.2.2 on 2023-07-03 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animaladoptreadycreate',
            name='animal_type',
            field=models.CharField(choices=[('other', 'Other'), ('cat', 'Cat'), ('dog', 'Dog')], max_length=30),
        ),
    ]
