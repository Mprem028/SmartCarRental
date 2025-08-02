from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Order, Message, Car
from .forms import OrderForm, CarForm, MessageForm, RegisterForm, LoginForm

# Homepage (optional)
def home(request):
    return render(request, 'home.html')

# Admin index view
@login_required
def adminIndex(request):
    return render(request, 'admin_index.html')

# Order list view
@login_required
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})

# Order edit view
@login_required
def order_edit(request, id):
    order = get_object_or_404(Order, id=id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'order_form.html', {'form': form})

# Order delete view
@login_required
def order_delete(request, id):
    order = get_object_or_404(Order, id=id)
    order.delete()
    return redirect('order_list')

# Car create view
@login_required
def car_create(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminIndex')
    else:
        form = CarForm()
    return render(request, 'car_form.html', {'form': form})

# Messages view
@login_required
def message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent successfully!")
            return redirect('message')
    else:
        form = MessageForm()
    all_messages = Message.objects.all()
    return render(request, 'message.html', {'form': form, 'messages': all_messages})

# Delete a message
@login_required
def msg_delete(request, id):
    msg = get_object_or_404(Message, id=id)
    msg.delete()
    return redirect('message')

# Login view
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('adminIndex')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')

# Register view
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! Please login.')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
