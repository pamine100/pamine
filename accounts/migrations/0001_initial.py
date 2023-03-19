# Generated by Django 4.1.4 on 2022-12-13 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=70)),
                ('password', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('phone', models.CharField(max_length=11)),
                ('address', models.CharField(max_length=256)),
                ('id_options', models.CharField(choices=[('Driver License', 'Driver License'), ('SSS ID', 'SSS ID'), ('Postal ID', 'Postal ID'), ('Student ID', 'Student ID')], max_length=64)),
                ('id_image', models.ImageField(upload_to='')),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
                ('updatedDate', models.DateTimeField(auto_now=True)),
                ('account_type', models.CharField(choices=[('Buyer', 'Buyer'), ('Seller', 'Seller')], max_length=64)),
            ],
        ),
    ]