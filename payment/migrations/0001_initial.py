# Generated by Django 2.1.3 on 2018-12-02 01:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=20)),
                ('value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terminal_id', models.CharField(max_length=20)),
                ('total_amount', models.FloatField()),
                ('order_token', models.CharField(max_length=20)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('modified_date', models.DateField(auto_now=True)),
                ('status', models.CharField(max_length=10)),
                ('token_response', models.CharField(max_length=100)),
                ('payment_link', models.CharField(max_length=50, null=True)),
                ('client', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.Client')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.Order'),
        ),
    ]
