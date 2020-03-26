from django.shortcuts import render, redirect

def login_successful(request):
    return render(request, "login_successful.html")
