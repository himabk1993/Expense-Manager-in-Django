from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import datetime
from .models import Expense, Shop, Category, PayMode
from signup.models import UserProfileInfo
from django.db.models import Sum

def add_expense(request):
    if request.method == 'POST':
        shop = request.POST.get('shop')
        print("shop_name ",shop)
        shop, shop_not_exists = Shop.objects.get_or_create(shop_name = shop)
        print("shop ",shop)
        print("shop.id ",shop.id)
        category = request.POST.get('category')
        print("category_name ",category)
        categ = Category.objects.get(pk = category)
        print("category ",categ)
        payed_by = request.POST.get('pay')
        print("payed ",payed_by)
        payed = PayMode.objects.get(pk = payed_by)
#        print("pay ",payed)
        item = request.POST.get('item')
        quantity = request.POST.get('quant')
        rate = request.POST.get('pay')
        purchase_date = request.POST.get('dt')
        description = request.POST.get('desc')
        print("description", description)
        entered_date = datetime.datetime.now()
        user = get_object_or_404(UserProfileInfo, pk = request.user.id)
        print("user ",user)
        expense = Expense(user = user, shop = shop, category = categ, payed_by = payed, item = item, quantity = quantity, rate = rate, purchase_date = purchase_date, description = description, entered_date = entered_date)
        expense.save()
        categories = Category.objects.all()
        paymodes = PayMode.objects.all()
        return render(request, 'expenseapp/expense.html', {'categories' : categories, 'paymodes' : paymodes })
    else:
        categories = Category.objects.all()
        paymodes = PayMode.objects.all()
        return render(request, 'expenseapp/expense.html', {'categories' : categories, 'paymodes' : paymodes })


def view_expense(request):
    if request.method == 'POST' :
        payment = request.POST.get('payment_type')
        purchased_date1 = request.POST.get('dt1')
        print("purchased_date1 ",purchased_date1)
        purchased_date2 = request.POST.get('dt2')
        print("purchased_date2 ",purchased_date2)
        records = Expense.objects.filter(user = request.user.id, payed_by = payment, purchase_date__range = (purchased_date1, purchased_date2))
        total_price = records.aggregate(total=Sum('rate'))
        total = total_price['total']
        print("records ",records)
        print("total ",total)
        paymodes = PayMode.objects.all()
        return render(request, 'expenseapp/expensereport.html', {'records' : records, 'total_price' : total, 'paymodes' : paymodes})

    else:
        print('request.id : ',request.user.id)
        records = Expense.objects.filter(user = request.user.id)
        for rec in records:
            print(rec)
        total_price = Expense.objects.all().aggregate(total=Sum('rate'))
        print('total : ', total_price['total'])
        total = total_price['total']
        paymodes = PayMode.objects.all()
        return render(request, 'expenseapp/expensereport.html', {'records' : records, 'total_price' : total, 'paymodes' : paymodes })
