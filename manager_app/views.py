from django.shortcuts import render

# Create your views here.
def manager_details(request):
    return render(request, "manager_details.html")

