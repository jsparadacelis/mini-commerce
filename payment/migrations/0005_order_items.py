# Generated by Django 2.1.3 on 2018-11-25 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_auto_20181125_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.TextField(default='products', max_length=300),
            preserve_default=False,
        ),
    ]
