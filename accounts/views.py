# Create your views here.
from django.shortcuts import render,redirect
from .forms import SignupForm
from django.contrib.auth import login

def signup(request):

    form = SignupForm()

    if request.method == 'POST':

        form = SignupForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request,user)

            return redirect('home')

    return render(request,'accounts/signup.html',{'form':form})