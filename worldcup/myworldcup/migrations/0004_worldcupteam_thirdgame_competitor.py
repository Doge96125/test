# Generated by Django 2.0.6 on 2018-06-29 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myworldcup', '0003_auto_20180629_0859'),
    ]

    operations = [
        migrations.AddField(
            model_name='worldcupteam',
            name='thirdgame_competitor',
            field=models.CharField(default='A1', max_length=20),
        ),
    ]
