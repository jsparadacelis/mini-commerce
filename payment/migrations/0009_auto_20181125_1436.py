# Generated by Django 2.1.3 on 2018-11-25 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0008_order_token_reponse'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='token_reponse',
            new_name='token_response',
        ),
    ]
