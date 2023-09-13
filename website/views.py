from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages  # for messages to interact with user/client
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.
def home(request):
    
    records = Record.objects.all()


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
        return render(request, 'home.html', {'records':records})

def login_user(request):    # request gets sent to back-end, request is when interacting with webpage
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully. Goodbye!")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():         # django is doing a lot of the work
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered. Welcome!")
            return redirect('home')

    else:   # not posting the form
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})  # posts the form into the register.html page

    return render(request, 'register.html', {'form':form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        # Lookup record
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You must be logged in to view that page...")
        return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id = pk)   # create record object contaning the respective pk
        delete_it.delete()  # delete the record object or pointer?
        messages.success(request, "Record has been deleted")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to perform this action")
        return redirect('home')


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record added")
                return redirect('home')

        return render(request, 'add_record.html', {'form':form})
    
    else: # not authenticated
        messages.success(request, "You must be logged in to perform this action")
        return redirect('home')


def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record) # instance will allow the form to be filled out with the old record
        if form.is_valid():
            form.save()
            messages.success(request, "Record updated")
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.success(request, "You must be logged in to perform this action")
        return redirect('home')


