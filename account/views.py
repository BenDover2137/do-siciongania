from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from django.contrib.auth import authenticate, login
from django.shortcuts import render

from account.forms import LoginForm, UserRegistrationForm


def user_login(request):
    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('succes')
                else:
                    return HttpResponse('konta nie ma')
            else:
                return HttpResponse('nie udalo sie uwierzytelnic')
    else:
        form=LoginForm()
    return render(request, 'account/login.html', {'form':form})

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html',{'section': 'dashboard'})

def register(request):
    if request.method=='POST':
        user_form=UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user=user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request,'account/registration_done.html', {'user_form': user_form})
    else:
        user_form=UserRegistrationForm
    return render(request, 'account/registration.html', {'user_form': user_form})
