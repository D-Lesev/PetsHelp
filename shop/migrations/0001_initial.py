# Generated by Django 4.2.2 on 2023-07-01 21:02

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import shop.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, validators=[shop.validators.check_for_letter])),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.DecimalValidator])),
                ('location', models.CharField(blank=True, max_length=200)),
                ('available_quantity', models.PositiveIntegerField()),
                ('main_photo', models.ImageField(upload_to='item_images/', validators=[shop.validators.resize_file_image])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
