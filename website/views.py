from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages  # for messages to interact with user/client

# Create your views here.
def home(request):
    # check to see if logging in
    if request.method == 'POST': # this is the method of the request (in home.html we set the form's method as POST)
        username = request.POST['username'] # this is from the name='password' in home.html
        password = request.POST['password'] # here we are setting the variables that we are getting from the request
        # Authenticate
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user) # login user
            messages.success(request, "Logged in successfully!") # we must still add messages to html
            return redirect('home') # redirect/return back to home page
        else:
            messages.success(request, "There was an error logging in...")
            return redirect('home')

    else:
        return render(request, 'home.html', {})

def login_user(request):    # request gets sent to back-end, request is when interacting with webpage
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('home')

