# Generated by Django 4.2 on 2023-06-13 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bolim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('rasm', models.FileField(upload_to='bolimlar')),
            ],
        ),
        migrations.CreateModel(
            name='Mahsulot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('narx', models.IntegerField()),
                ('min_miqdor', models.PositiveSmallIntegerField(default=1)),
                ('davlat', models.CharField(max_length=100)),
                ('brend', models.CharField(max_length=30)),
                ('kafolat', models.CharField(max_length=30)),
                ('matn', models.TextField()),
                ('chegirma', models.PositiveSmallIntegerField(default=0)),
                ('bolim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.bolim')),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasm', models.FileField(upload_to='mahsulotlar')),
                ('mahsulot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.mahsulot')),
            ],
        ),
    ]
