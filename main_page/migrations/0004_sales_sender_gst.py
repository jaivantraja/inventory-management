# Generated by Django 4.2.1 on 2023-05-21 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0003_purchase_cost_sales_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='sender_gst',
            field=models.CharField(default='None', max_length=15),
        ),
    ]