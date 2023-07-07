# Generated by Django 4.2.2 on 2023-07-07 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0012_shareanimalmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shareanimalmodel',
            name='address',
        ),
        migrations.AddField(
            model_name='shareanimalmodel',
            name='city',
            field=models.CharField(default='Plovdiv', max_length=30),
        ),
        migrations.AddField(
            model_name='shareanimalmodel',
            name='province',
            field=models.CharField(default='Plovdiv', max_length=30),
        ),
        migrations.AlterField(
            model_name='adoptionhomemodel',
            name='animal_type',
            field=models.CharField(choices=[('other', 'Other'), ('cat', 'Cat'), ('dog', 'Dog')], max_length=30),
        ),
    ]
