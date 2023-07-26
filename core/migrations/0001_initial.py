# Generated by Django 4.2.3 on 2023-07-24 12:19

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
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='uploads/')),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=30)),
                ('mobile', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('nickname', models.CharField(max_length=30)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]