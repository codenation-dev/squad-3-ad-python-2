# Generated by Django 2.2.3 on 2019-07-28 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commission', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commission',
            name='year',
            field=models.IntegerField(default=2019),
            preserve_default=False,
        ),
    ]