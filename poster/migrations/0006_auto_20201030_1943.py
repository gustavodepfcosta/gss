# Generated by Django 3.1.2 on 2020-10-30 19:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('poster', '0005_auto_20201030_1157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateField(auto_now=True, verbose_name='Modified')),
                ('active', models.DateTimeField(default=datetime.datetime(2020, 10, 30, 19, 43, 2, 971107, tzinfo=utc), verbose_name='Active')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('age', models.IntegerField(verbose_name='Age')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='contact',
            name='active',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 30, 19, 43, 2, 971107, tzinfo=utc), verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='active',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 30, 19, 43, 2, 971107, tzinfo=utc), verbose_name='Active'),
        ),
    ]
