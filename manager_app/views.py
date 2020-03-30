from django.shortcuts import render, redirect
# trying some things out with AJAX requests
from django.http import JsonResponse
from django.core import serializers
from .forms import ManagerForm
from .models import Manager

# Create your views here.
def index_view(request):
    # instantiate the form object so it can be passed in to the view
    form = ManagerForm()
    managers = Manager.objects.all()
    context = {
        "form": form,
        "managers": managers,
    }
    return render(request, "manager_list.html", context)

def post_manager(request):
    if request.is_ajax and request.method == "POST":
        # get the form data and assign it as a form object
        form = ManagerForm(request.POST)

        # now use the built in form validation to verify our data passed in with the POST
        if form.is_valid():
            print("form is valid - creating manager")
            # we can now process the data that came in the POST dictionary...but we access the "clean" data
            #   using the form.cleaned_data attribute / property
            manager_exists = Manager.objects.filter(first_name = form.cleaned_data['first_name'], last_name = form.cleaned_data['last_name'])
            if len(manager_exists) > 0:
                print(f"user already exists - manager id: {manager_exists[0].id}")
                return JsonResponse({"error": "That manager already exists"}, status = 200)

            # save this in the database and assign the returned instance of the manager object to a variable
            instance = form.save()

            # serialize the data in a json format
            json_instance = serializers.serialize('json', [instance, ])
            # print(f"instance id just created: {instance.id}")
            print(f"manager json just created: {json_instance}")

            # send the serialized instance back to the client
            return JsonResponse({"instance": json_instance}, status = 200)
        else:
            # form wasn't valid, let them try again
            return JsonResponse({"error": form.errors}, status = 400)

    return JsonResponse({"error": "An unknown error occured while saving the Manager"}, status = 400)

# update the manager object and save to DB
def update(request, manager_id):
    print("in manager update")
    if request.is_ajax and request.method == "POST":
        # get the form data and assign it as a form object
        form = ManagerForm(request.POST)

        # now use the built in form validation to verify our data passed in with the POST
        if form.is_valid():
            print("form is valid - creating manager")

            if not "is_active" in form.cleaned_data:
                form.cleaned_data['is_active'] = False

            # save this in the database and assign the returned instance of the manager object to a variable
            instance = form.save()
            return redirect(f"/manager/details/{instance.id}")

def details(request, manager_id):
    print("in manager details")
    # Get the manager that matches this id
    manager = Manager.objects.get(id=manager_id)
    # manager = {
    #     "id": 6,
    #     "first_name": "Test",
    #     "last_name": "Manager",
    #     "title": "Low level manager",
    #     "active": False,
    # }
    context = {
        # "is_add_manager": False,
        "manager": manager,
    }
    return render(request, "manager_details.html", context)

# These are some old views priot to me trying out the AJAX requests
# def view_list(request):
#     print("in manager view_list")
#     return render(request, "manager_list.html")

# def add(request):
#     print("in manager add")
#     # using blank values to simplify the HTML page we will render
#     manager = {
#         "id": 5,
#         "first_name": "",
#         "last_name": "",
#         "title": "",
#         "active": True,
#     }
#     context = {
#         "is_add_manager": True,
#         "manager": manager,
#     }
#     return render(request, "manager_details.html", context)

# def create(request):
#     print("in manager create")
#     manager_id = 9
#     return redirect(f"/manager/details/{manager_id}")
