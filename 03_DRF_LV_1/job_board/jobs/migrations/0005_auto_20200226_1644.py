# Generated by Django 3.0.3 on 2020-02-26 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20200226_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='joboffer',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]