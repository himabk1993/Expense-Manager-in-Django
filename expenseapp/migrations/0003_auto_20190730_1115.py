# Generated by Django 2.2.3 on 2019-07-30 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expenseapp', '0002_expense_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='category_name',
        ),
        migrations.RemoveField(
            model_name='expense',
            name='shop_name',
        ),
        migrations.AddField(
            model_name='expense',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='expenseapp.Category'),
        ),
        migrations.AddField(
            model_name='expense',
            name='shop',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='expenseapp.Shop'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='payed_by',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='expenseapp.PayMode'),
        ),
    ]
