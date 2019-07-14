# Generated by Django 2.2.3 on 2019-07-12 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('minimum_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('minimum_percentage', models.FloatField()),
                ('maximum_percentage', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Útima atualização')),
            ],
        ),
    ]
