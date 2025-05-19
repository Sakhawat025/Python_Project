from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import CustomUser
from django.shortcuts import render
from myapp.models import CarWashBooking, CarRental 
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')
        image = request.FILES.get('image')  # get uploaded image
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('signup')
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('signup')
        user = CustomUser.objects.create_user(email=email, username=username, password=password, user_type=user_type)
        if image:
            user.image = image
            user.save()
        user.backend = 'users.backends.EmailBackend'
        login(request, user)
        return redirect('home')
    return render(request, 'Auth/signup.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')  # or 'home' or any other page
        else:
            messages.error(request, "Invalid email or password.")
    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')




@login_required
def profile_view(request):
    bookings = CarWashBooking.objects.filter(user=request.user)
    rents = CarRental.objects.filter(user=request.user)
    return render(request, 'Auth/profile.html', {
        'user': request.user,
        'bookings': bookings,
        'rents': rents,
    })
