# Generated by Django 2.2.3 on 2019-07-31 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenseapp', '0011_auto_20190731_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='description',
            field=models.CharField(default='NILL', max_length=1000, verbose_name='Extra notes on the purchase'),
        ),
    ]