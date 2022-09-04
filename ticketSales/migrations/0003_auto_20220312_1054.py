# Generated by Django 3.2.9 on 2022-03-12 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketSales', '0002_auto_20220217_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timemodel',
            name='StartDateTime',
            field=models.DateTimeField(verbose_name='تاریخ برگزاری'),
        ),
        migrations.AlterField(
            model_name='timemodel',
            name='seats',
            field=models.IntegerField(verbose_name='تعداد صندلی'),
        ),
        migrations.AlterField(
            model_name='timemodel',
            name='statuses',
            field=models.IntegerField(choices=[(1, 'فروش بلیط شروع شده است'), (2, 'فروش بلیط تمام شده است'), (3, 'این سانس کنسل شده است'), (4, 'درحال فروش بلیط')], verbose_name='وضعیت'),
        ),
    ]
