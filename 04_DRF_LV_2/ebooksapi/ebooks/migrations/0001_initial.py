# Generated by Django 3.0.3 on 2020-02-28 13:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('author', models.CharField(max_length=60)),
                ('descriptiom', models.TextField()),
                ('publication_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('ratiing', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxLengthValidator(5)])),
                ('review', models.TextField(blank=True, null=True)),
                ('review_author', models.CharField(blank=True, max_length=8, null=True)),
                ('ebook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='ebooks.Ebook')),
            ],
        ),
    ]
