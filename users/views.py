from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import forms
from writenotes import models

def index(request):
    return redirect("login")

def register_user(request):
    """User registration"""
    loggedin_user = request.user
    if loggedin_user.is_authenticated:
        return redirect("home")
    else:
        if request.method == "POST":
            form = forms.RegistrationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect("home")
        else:
            form = forms.RegistrationForm()
        return render(request, "registration/register.html", {'form': form})


def login_user(request):
    """User login"""
    loggedin_user = request.user
    if loggedin_user.is_authenticated:
        return redirect("home")
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful.')
                return redirect('home')
            else:
                messages.error(request, 'Unable to login.')
        
        return render(request, 'registration/login.html')

def logout_user(request):
    """User logout"""
    logout(request)
    messages.success(request, 'Logout successful.')
    return redirect("login")

@login_required
def home(request):
    """Home page"""
    user = request.user
    notes = models.Note.objects.get_queryset().filter(author=user)
    collections = models.NoteCollection.objects.get_queryset().filter(author=user)
    if request.method == "POST":
        form = forms.NoteCollectionCreationForm(request.POST)
        if form.is_valid():
            collection = form.save(commit=False)
            collection.author = request.user
            collection.save()
            return redirect(request.META['HTTP_REFERER'])
    return render(request, 'home.html', {'user': user, 'notes': notes, 'collections': collections})
