from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login as auth_login
from django.contrib import messages
from .forms import RegisterForm  # Ensure this matches your actual form name
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def registration(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Log the user in after registration
            messages.success(request, 'Account created successfully')
            return redirect('homePage')  # Redirect as needed
        else: print(form.errors)
    context = {'form': form}
    return render(request, 'register_user.html', context)

@csrf_exempt
def login_in(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Ensure this is what you use for login
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)  # Use 'username' for email

        if user is not None:
            auth_login(request, user)
            return redirect('homePage')
        else:
            messages.info(request, 'Username or Password is incorrect')

    template = 'login_user.html'
    context = {}
    return render(request, template, context)


@csrf_exempt
def logoutUser(request):
    logout(request)
    return redirect('login_in')
