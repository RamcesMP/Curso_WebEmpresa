# Generated by Django 3.1 on 2022-12-06 21:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publicado',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]