# Generated by Django 4.1.5 on 2023-01-20 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='isbn',
            field=models.CharField(max_length=13, unique=True),
        ),
    ]