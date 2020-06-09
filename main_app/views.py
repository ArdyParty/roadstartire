from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.views.generic import ListView
from .models import Tire, Cart, CartDetail

# Create your views here.

def home(req):
  return render(req, 'home.html')

def signup(req):
    #error_message = ''
    if req.method == 'POST':
        # This is how to create a 'user' form object that includes the data from the browser
        form = UserCreationForm(req.POST)
        if form.is_valid():
            user = form.save() # Add the user to the database
            login(req, user) # Log a user in via code
            return redirect('home')
    #     else:
    #         error_message = 'Invalid sign up - try again'
    # # A bad POST or a GET request, so render signup.html with an empty form
    # form = UserCreationForm()
    # context = {'form': form, 'error_message': error_message}
    # return render(req, 'registration/signup.html', context) # redirect to login page
    return render(req, 'signup.html') # redirect to login page

def login(req):
  return render(req, 'login.html')

def account(req):
  user = req.user
  carts = Cart.objects.filter(user_id=req.user.id)
  return render(req, 'account.html', { 'user': user, 'carts': carts })

def about(req):
  return render(req, 'about.html')

def services(req):
  return render(req, 'services.html')

def tires(req):
  return render(req, 'tires.html')

def cartDetail(req):
  return render(req, 'cart.html')

def orderDetail(req, cart_id):
  order = Cart.objects.get(id=cart_id)
  order_detail = CartDetail.objects.filter(cart_id=cart_id)
  return render(req, 'order_detail.html', { 'order': order, 'order_detail': order_detail })

def orderCancel(req, cart_id):
  order = Cart.objects.get(id=cart_id)
  order.status = 2
  order.save()
  return redirect('order_detail', cart_id)


class TireList(ListView):
  model = Tire