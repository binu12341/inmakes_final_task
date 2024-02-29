# Generated by Django 4.2.10 on 2024-02-27 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_title', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('category', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('movie_title',),
            },
        ),
        migrations.CreateModel(
            name='User_registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=240, null=True)),
                ('lastname', models.CharField(max_length=240, null=True)),
                ('username', models.CharField(max_length=240, null=True, unique=True)),
                ('email', models.EmailField(max_length=240, null=True, unique=True)),
                ('password', models.CharField(max_length=240, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Add_movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('poster', models.ImageField(blank=True, upload_to='gallery')),
                ('description', models.TextField(max_length=200, null=True)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('actors', models.CharField(max_length=200, null=True)),
                ('YouTube_trailer_link', models.CharField(max_length=200, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Movieapp.category')),
            ],
            options={
                'verbose_name': 'add movies',
                'verbose_name_plural': 'add movies',
                'ordering': ('movie_title',),
            },
        ),
    ]