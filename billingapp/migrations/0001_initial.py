# Generated by Django 3.0.5 on 2020-04-09 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateField()),
                ('is_active', models.BooleanField(default=False)),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_label', models.CharField(max_length=100, unique=True)),
                ('user_address', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(auto_now_add=True)),
                ('end_date', models.DateField()),
                ('payment_status', models.CharField(max_length=100)),
                ('payment_mode', models.CharField(max_length=100)),
                ('tax_amount', models.FloatField()),
                ('payment_address', models.CharField(max_length=100)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billingapp.Product')),
                ('user', models.ManyToManyField(blank=True, null=True, to='billingapp.User')),
            ],
        ),
    ]