# Generated by Django 3.1 on 2020-12-09 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_auto_20201207_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='county',
            field=models.CharField(blank=True, default=1234, max_length=80),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='street_address2',
            field=models.CharField(blank=True, default=123, max_length=80),
            preserve_default=False,
        ),
    ]
