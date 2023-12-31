# Generated by Django 4.2.5 on 2023-10-11 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('villageapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pimage',
            field=models.ImageField(default=0, upload_to='image'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='cat',
            field=models.IntegerField(choices=[(1, 'crop protection'), (2, 'Crop neutritions'), (3, 'Seeds')], verbose_name='categories'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Product Name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pdetails',
            field=models.CharField(max_length=50, verbose_name='Product Deteils'),
        ),
    ]
