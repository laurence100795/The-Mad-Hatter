# Generated by Django 3.1 on 2020-10-27 20:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20201023_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=50, unique=True),
        ),
    ]
