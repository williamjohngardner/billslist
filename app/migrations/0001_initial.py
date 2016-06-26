# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-26 19:28
from __future__ import unicode_literals

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
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('title', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('photos', models.ImageField(blank=True, null=True, upload_to='listing_photos', verbose_name='Listing Photo')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=30)),
                ('street_address', models.CharField(max_length=30)),
                ('street_address_2', models.CharField(max_length=30, null=True)),
                ('city', models.CharField(max_length=35)),
                ('state', models.CharField(max_length=15)),
                ('zip_code', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='profile_photos', verbose_name='Profile Photo')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory', models.CharField(max_length=20)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Category')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='location_pref',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Region'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='listing',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Region'),
        ),
        migrations.AddField(
            model_name='listing',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Profile'),
        ),
        migrations.AddField(
            model_name='listing',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.SubCategory'),
        ),
    ]
