# Generated by Django 3.1.6 on 2021-02-04 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='price',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
