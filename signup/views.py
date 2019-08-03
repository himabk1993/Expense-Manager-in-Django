from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login,logout, authenticate
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from signup.forms import UserForm, UserProfileInfoForm
from expenseapp.models import Category, PayMode
# Create your views here.

def index(request):
    return render(request, 'signup/index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in")

@login_required
def user_logout(request):
    logout(request)
    return reverse(index)

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('uploaded picture')
                profile.profile_pic = request.FILES('profile_pic')
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'signup/registration.html',{'user_form' : user_form,
        'profile_form' : profile_form, 'registered' : registered})

def user_login(request):
    print('entered')
    print("request.id", request.user.id)
    if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user:
            if user.is_active:
                print("active")
                login(request, user)
                print("done the function")
                return redirect('../expenseapp/expense')

            else:
                return HttpResponse('Your account is inactive !!!')
        else:
            print('someone tried to login and failed')
            print('They used username {} and password {}'.format(username, password))
            return HttpResponse('Invalid login details given')
    else:
        print('reached')
        return render(request, 'signup/login.html',{})
