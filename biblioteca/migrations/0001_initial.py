# Generated by Django 4.1.5 on 2023-01-17 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=13)),
                ('autor', models.CharField(max_length=30)),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('datapub', models.DateField()),
            ],
        ),
    ]

