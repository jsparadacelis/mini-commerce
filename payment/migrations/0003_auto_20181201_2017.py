# Generated by Django 2.1.3 on 2018-12-02 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_auto_20181201_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_link',
            field=models.CharField(max_length=200),
        ),
    ]
