# Generated by Django 4.0.4 on 2022-10-17 02:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('WebApp', '0002_posts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='image',
        ),
        migrations.AlterField(
            model_name='posts',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='posts',
            name='body',
            field=models.TextField(max_length=1000),
        ),
    ]
