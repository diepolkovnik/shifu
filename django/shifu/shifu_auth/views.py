from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.conf import  settings

# Create your views here.

def index(request):
    return render(request, 'shifu_auth/index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()

    context = {'form' : form}
    return render(request, 'registration/register.html', context)

def sendmail(request):
     send_mail(
        'subject',
        'message',
        'localhost',
        ['localhost'],
        fail_silently=False
    )