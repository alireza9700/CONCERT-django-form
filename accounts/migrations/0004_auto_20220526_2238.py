# Generated by Django 3.2.9 on 2022-05-26 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20220405_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='Gender',
            field=models.IntegerField(choices=[(1, 'مرد'), (2, 'زن')], verbose_name='جنسیت'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='ProfileImage',
            field=models.ImageField(upload_to='ProfileImages/', verbose_name='عکس'),
        ),
    ]
