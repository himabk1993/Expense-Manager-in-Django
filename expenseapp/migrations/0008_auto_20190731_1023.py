# Generated by Django 2.2.3 on 2019-07-31 10:23

from django.db import migrations

def insert_record(apps, schema_editor):

    Category = apps.get_model('expenseapp', 'Category')
    PayMode = apps.get_model('expenseapp', 'PayMode')

    category_list = ['Grocery', 'Travel', 'Entertainment', 'Other']
    paymode_list = ['Cash', 'Card']

    for categ in category_list:
        categories = Category.objects.get_or_create(category_name = categ)

    for pay in paymode_list:
        pays = PayMode.objects.get_or_create(payed_by = pay)


class Migration(migrations.Migration):

    dependencies = [
        ('expenseapp', '0007_auto_20190730_1347'),
    ]

    operations = [
        migrations.RunPython(insert_record),
    ]
