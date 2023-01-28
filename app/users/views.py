from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from unlimited.models import Technique, Character
# Create your views here.
def register(request):
    if request.method=="POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            new_username = form.cleaned_data.get("username")
            messages.success(request,f"{new_username}, your account has been created!")
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect("unlimited-home")
    else:
        form = UserRegisterForm()
    return render(request,"users/register.html",{"form":form})

@login_required
def profile(request):
    if request.method=="POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your info has been updated!")
            return redirect("profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        
    context = {
        "u_form":u_form,
        "p_form":p_form,
        "techniques": Technique.objects.all(),
        "characters": Character.objects.all(),
    }
    return render(request,"users/profile.html",context)
