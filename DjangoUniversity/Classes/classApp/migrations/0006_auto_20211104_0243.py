# Generated by Django 3.2.9 on 2021-11-04 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classApp', '0005_auto_20211104_0242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='djangoclasses',
            name='Duration',
            field=models.FloatField(blank=True, default='1.00', max_length=10),
        ),
        migrations.AlterField(
            model_name='djangoclasses',
            name='Title',
            field=models.CharField(choices=[('HTML/CSS', 'HTML/CSS'), ('JavaScript', 'JavaScript'), ('Python', 'Python')], max_length=50),
        ),
    ]
