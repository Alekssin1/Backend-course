from django.shortcuts import render, redirect
from .forms import SubscribeForm
from django.contrib import messages

def subscribe(request):
    print("*"*30)
    print(request.method)
    print("*"*30)
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have subscribed successfully!')
        else:
            messages.error(request, 'Please enter a valid email address.')
    return redirect('home')