# Generated by Django 3.1.2 on 2020-11-04 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20201103_0739'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='confirmation',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]
