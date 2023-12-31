# Generated by Django 4.2 on 2023-06-20 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
        ('buyurtma', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manzil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('davlat', models.CharField(max_length=50)),
                ('shahar', models.CharField(max_length=50)),
                ('manzil', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=50)),
                ('asosiy', models.BooleanField(default=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.account')),
            ],
        ),
        migrations.CreateModel(
            name='Buyurtma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sana', models.DateField(auto_now_add=True)),
                ('holat', models.CharField(max_length=50)),
                ('manzil', models.CharField(max_length=50)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.account')),
                ('savat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyurtma.savat')),
            ],
        ),
    ]
