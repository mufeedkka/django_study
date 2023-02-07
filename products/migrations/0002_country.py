# Generated by Django 4.1.6 on 2023-02-07 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('capital', models.CharField(max_length=100)),
                ('area', models.IntegerField(help_text='(in square kilometers)')),
            ],
        ),
    ]
