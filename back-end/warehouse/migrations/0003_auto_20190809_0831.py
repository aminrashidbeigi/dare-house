# Generated by Django 2.2.4 on 2019-08-09 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0002_auto_20190809_0831'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='segmentproduct',
            unique_together={('segment', 'product')},
        ),
    ]