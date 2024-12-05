# Generated by Django 4.2.16 on 2024-11-21 10:30

import ckeditor_uploader.fields
from django.db import migrations, models
import kollej_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Directions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name="Yo'nalish nomi")),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(verbose_name="Yo'nalish matni")),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Leadership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=56, verbose_name="\\To'liq isim")),
                ('acceptions', models.CharField(max_length=56, verbose_name='Qabul kunlari')),
                ('position', models.CharField(max_length=26, verbose_name='lavozim')),
                ('phone_number', models.CharField(max_length=26, verbose_name='Telfon raqam')),
                ('email', models.CharField(max_length=56)),
                ('image', models.ImageField(upload_to='img/', validators=[kollej_app.models.validate_file_size])),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_update', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_type', models.CharField(choices=[('1', 'news'), ('2', 'events')], default='1', max_length=20)),
                ('image', models.ImageField(upload_to='img/', validators=[kollej_app.models.validate_file_size])),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Yangilik matni')),
                ('views', models.IntegerField(default=0, verbose_name="ko'rishlar soni")),
                ('title', models.CharField(max_length=255)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_update', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='OpenData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('pdf_file', models.FileField(upload_to='')),
                ('open_method', models.CharField(choices=[('1', "ochiq ma'lumotlar"), ('2', 'nizom')], max_length=20)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Requisites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_name', models.CharField(max_length=100, verbose_name='kollej nomi')),
                ('address', models.CharField(max_length=100, verbose_name='manzil')),
                ('phone', models.CharField(max_length=100, verbose_name='tellfon raqam')),
                ('email', models.CharField(max_length=100, verbose_name='poschta manzil')),
                ('bank_account', models.CharField(max_length=100, verbose_name='bank hisob raqam')),
                ('fax', models.CharField(max_length=100)),
                ('bank', models.CharField(max_length=100)),
                ('mfo', models.CharField(max_length=100)),
                ('INN', models.CharField(max_length=100)),
                ('OKONX', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]