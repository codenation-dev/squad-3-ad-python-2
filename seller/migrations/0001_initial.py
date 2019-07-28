# Generated by Django 2.2.3 on 2019-07-28 01:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('plan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(blank=True, max_length=250)),
                ('age', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=254)),
                ('cpf', models.CharField(max_length=14)),
                ('phone', models.CharField(max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Útima atualização')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller_plan', to='plan.Plan')),
            ],
        ),
    ]
