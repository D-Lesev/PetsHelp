# Generated by Django 4.2.2 on 2023-07-09 20:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ShareAnimalModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('notes', models.TextField(blank=True, null=True)),
                ('province', models.CharField(default='Plovdiv', max_length=30)),
                ('city', models.CharField(default='Plovdiv', max_length=30)),
                ('main_photo', models.ImageField(upload_to='help_animals/%Y/%m/%d/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'ShareAnimal',
            },
        ),
        migrations.CreateModel(
            name='AdoptPetModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_pet', models.CharField(max_length=30)),
                ('location', models.CharField(blank=True, max_length=50)),
                ('pet_story', models.TextField()),
                ('photo', models.ImageField(upload_to='happy_adopted/')),
                ('date_of_adoption', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'AdoptPet',
            },
        ),
        migrations.CreateModel(
            name='AdoptionHomeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('province', models.CharField(max_length=25)),
                ('city', models.CharField(max_length=25)),
                ('picture', models.ImageField(upload_to='adoption_homes/')),
                ('animal_type', models.CharField(choices=[('cat', 'Cat'), ('other', 'Other'), ('dog', 'Dog')], max_length=30)),
                ('description', models.TextField(blank=True)),
                ('start_period', models.DateField()),
                ('end_period', models.DateField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'AdoptionHome',
            },
        ),
    ]
