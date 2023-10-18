# Generated by Django 4.2.5 on 2023-10-09 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('cat', models.IntegerField()),
                ('pdetails', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
