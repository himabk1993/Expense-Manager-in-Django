# Generated by Django 2.2.3 on 2019-07-31 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenseapp', '0008_auto_20190731_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='description',
            field=models.CharField(default='', max_length=1000, verbose_name='Extra notes on the purchase'),
        ),
    ]
