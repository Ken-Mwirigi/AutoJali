from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import CarOwners, BreakDownDetails,Order
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Handle Login for Car Owners


# views.py


def register_owner(request):
    if request.method == 'POST':
        # Create a User instance first

        # Create a CarOwner instance associated with the User
        car_owner = CarOwners(
            fullname=request.POST['fullname'],
            phone=request.POST['contact-number'],
            email=request.POST['email'],
            username=request.POST['username'],
            password=request.POST['password']
           # password=make_password(request.POST['password'])
        )
        car_owner.save()
        return redirect('/login')
    else:
        return render(request, 'owner-register.html')


def car_owner_login(request):
    if request.method == 'POST':
        if CarOwners.objects.filter(
          username=request.POST.get('username'), # Use .get() to avoid errors if the key is missing
          password = request.POST.get('password')
        ).exists():
            return render(request, 'owner_dashboard.html')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')





def driver_login(request):
    if request.method == 'POST':
        if BreakDownDetails.objects.filter(
        username = request.POST['username'],
        password = request.POST['password']
        ).exists():
            return render(request, 'after_driver_login.html')
        else:
            return render(request, 'login-driver.html')
    else:
        return render(request, 'login-driver.html')



# Handle Registration for Car Owners

# Handle Registration for Car Owners
# views.py

def register_driver(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        contact_number = request.POST['contact_number']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
       # password = make_password(request.POST['password'])  # Ensure password is hashed
        license = request.FILES['license']
        insurance = request.FILES['insurance']
        vehicle_model = request.POST['vehicle_model']
        vehicle_registration = request.POST['vehicle_registration']
        vehicle_image = request.FILES['vehicle_images']

        # Save details to the database
        breakdown_driver = BreakDownDetails(
            fullname=fullname,
            contact_number=contact_number,
            email=email,
            username=username,
            password=password,
            license=license,
            insurance=insurance,
            vehicle_model=vehicle_model,
            vehicle_registration=vehicle_registration,
            vehicle_image=vehicle_image,
        )
        breakdown_driver.save()
        return redirect('login-driver')  # Redirect to login page

    return render(request, 'register-driver.html')

# Base view (if needed for navigation or other purposes)
def base(request):
    return render(request, 'base.html')

# Index page view
def index(request):
    return render(request, 'index.html')

# Register Type view (for selecting registration type)
def register_type(request):
    return render(request, 'register-type.html')
def confirm_delete(request):
    return render(request, 'confirm_delete.html')

# Register Driver view

# Login page view (if separate from car_owner_login)


# views.py
from django.shortcuts import render, redirect
from .models import Order
from django.http import HttpResponse

def owner_dashboard(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        phone = request.POST.get('phone')
        pickup_location = request.POST.get('pickup_location')
        drop_off_location = request.POST.get('drop_off_location')
        fare = request.POST.get('fare')
        driver_name = request.POST.get('driver_name') # Assuming driver_id corresponds to driver's name

        # Create a new order object and save it to the database
        order = Order(
            fullname=fullname,
            phone=phone,
            pickup_location=pickup_location,
            drop_off_location=drop_off_location,
            fare=fare,
            driver=driver_name
        )
        order.save()
        return redirect('payment')



    return render(request, 'owner_dashboard.html')




 # Ensure user is logged in
# views.py

def payment(request):
    order = Order.objects.all()  # Fetch all orders from the database
    return render(request, 'payment.html', {'orders': order})  # Pass orders to the template

def delete_order(request, id):
    order = get_object_or_404(Order, id=id)
    if request.method == 'POST':  # Confirmation step (optional)
        order.delete()
        return redirect('payment')  # Redirect to the orders list after deletion

    return render(request, 'confirm_delete.html', {'order': order})

from django.shortcuts import get_object_or_404, redirect, render
from .models import Order

def edit_order(request, id):
    order = get_object_or_404(Order, id=id)
    if request.method == 'POST':
        # Update the order details from the form
        order.fullname = request.POST.get('fullname')
        order.phone = request.POST.get('phone')
        order.pickup_location = request.POST.get('pickup_location')
        order.drop_off_location = request.POST.get('drop_off_location')
        order.fare = request.POST.get('fare')
        order.driver = request.POST.get('driver')

        order.save()
        return redirect('payment')  # Redirect to the orders list after updating

    return render(request, 'edit_order.html', {'order': order})

def driver_dashboard(request):
    return render(request, 'driver-dashboard.html')

def after_driver_login(request):
    return render(request, 'after_driver_login.html')
def view_driver_details(request):
    detail = BreakDownDetails.objects.values('fullname','contact_number','email','license','insurance','vehicle_model','vehicle_number','vehicle_registration','vehicle_image')  # Fetch all orders from the database
    return render(request, 'view_driver_details.html', {'details': detail})  # Pass orders to the template


def view_orders(request):
    d_order = Order.objects.all()  # Fetch all orders from the database
    return render(request, 'view_orders.html', {'d_orders': d_order})  # Pass orders to the template

