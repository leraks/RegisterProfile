from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login,authenticate,logout as django_logout
from django.contrib import messages

from .forms import CreateUserForm



def register(request):
    form = CreateUserForm()
    error_form = ""


    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        print(form.errors)


        if form.is_valid():
            form.save()
            messages.success(request,'Account created')
            return redirect('login')
        else:
            messages.error(request, 'An error registration ')
            error_form = form.errors
            form = CreateUserForm()


    context = {'forms':form,'error_form':error_form}
    return render(request,template_name='register/register.html', context=context)


def loginuser(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST,data=request.POST)
        print(form.errors)
        if form.is_valid():

            username = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            user = authenticate(username=username,password=upass)
            if user is not None:
                login(request,user)
                return redirect('/room')
    else:
        form =AuthenticationForm()
    context  = {
        'forms':form,
    }

    return render(request,template_name='login/login.html', context=context)

def logout(request):
    django_logout(request)
    return redirect('/login')