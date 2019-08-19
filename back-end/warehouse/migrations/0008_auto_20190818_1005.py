# Generated by Django 2.2.4 on 2019-08-18 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0007_auto_20190818_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(blank=True, through='warehouse.OrderProduct', to='warehouse.Product'),
        ),
        migrations.AddField(
            model_name='segment',
            name='products',
            field=models.ManyToManyField(blank=True, through='warehouse.SegmentProduct', to='warehouse.Product'),
        ),
    ]
