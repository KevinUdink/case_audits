from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core import serializers
from .forms import AttorneyForm, AttorneyDetailForm
from .models import Attorney

# Create your views here.
def view_list(request):
    print("in attorney view_list")
    attorneys = Attorney.objects.all()
    form = AttorneyForm()
    context = {
        "attorneys": attorneys,
        "form": form,
    }
    return render(request, "attorney_list.html", context)

def details(request, attorney_id):
    print(f"in attorney details: {attorney_id}")
    # Get the attorney that matches this id
    attorney = Attorney.objects.get(id = attorney_id)
    # print(f"\tattorney details: {attorney}")
    form = AttorneyDetailForm(instance=attorney)

    context = {
        "is_add_attorney": False,
        "attorney": attorney,
        "form": form,
    }
    return render(request, "attorney_details.html", context)

def post_attorney(request):
    if request.is_ajax and request.method == "POST":
        # get the form data and assign it as a form object
        form = AttorneyForm(request.POST)

        # now use the built in form validation to verify our data passed in with the POST
        if form.is_valid():
            print("form is valid - creating attorney")
            # we can now process the data that came in the POST dictionary...but we access the "clean" data
            #   using the form.cleaned_data attribute / property
            attorney_exists = Attorney.objects.filter(first_name = form.cleaned_data['first_name'], last_name = form.cleaned_data['last_name'])
            if len(attorney_exists) > 0:
                print(f"Attorney already exists - attorney id: {attorney_exists[0].id}")
                return JsonResponse({"error": "That atorney already exists"}, status = 400)

            # save this in the database and assign the returned instance of the manager object to a variable
            instance = form.save()

            # serialize the data in a json format
            json_instance = serializers.serialize('json', [instance, ])
            # print(f"instance id just created: {instance.id}")
            print(f"Attorney json just created: {json_instance}")

            # send the serialized instance back to the client
            return JsonResponse({"instance": json_instance}, status = 200)
        else:
            # form wasn't valid, let them try again
            return JsonResponse({"error": form.errors}, status = 400)

    return JsonResponse({"error": "An unknown error occured while posting the new Attorney"}, status = 400)

def add(request):
    print("in attorney add")
    form = AttorneyForm()

    context = {
        "is_add_attorney": True,
        "form": form
    }
    return render(request, "attorney_details.html", context)

def create(request):
    print("in attorney create")
    if request.method == "POST":
        # get the form data and assign it as a form object
        form = AttorneyForm(request.POST)

        # now use the built in form validation to verify our data passed in with the POST
        if form.is_valid():
            print("form is valid - creating attorney")
            # we can now process the data that came in the POST dictionary...but we access the "clean" data
            #   using the form.cleaned_data attribute / property
            attorney_exists = Attorney.objects.filter(first_name = form.cleaned_data['first_name'], last_name = form.cleaned_data['last_name'])
            if len(attorney_exists) > 0:
                print(f"That attorney already exists - attorney id: {attorney_exists[0].id}")
                # redirect to the attorney that already exists
                return redirect(f"/attorney/details/{attorney_exists[0].id}")

            # save this in the database and assign the returned instance of the manager object to a variable
            instance = form.save()
            print(f"instance id just created: {instance.id}")
            return redirect(f"/attorney/details/{instance.id}")
        else:
            # form wasn't valid, let them try again
            print("Form is invalid - Try again!")
            # send the form back to show the errors as well as repopulate with the data they entered
            return render(request, "/attorney/add", {"form": form})

    # Since this is not a post request, redirect them to the attorney list
    return redirect("/attorney/")
    
# update the attorney object and save to DB
def update(request, attorney_id):
    print("in attorney update")
    if request.method == "POST":
        attorney = Attorney.objects.get(id = attorney_id)

        # get the form data and apply it to the instance and then assign it as a form object
        form = AttorneyDetailForm(request.POST, instance=attorney)

        # now use the built in form validation to verify our data passed in with the POST
        if form.is_valid():
            print("form is valid - updating attorney")
            
            # save this in the database and assign the returned instance of the manager object to a variable
            instance = form.save()
            return redirect(f"/attorney/details/{instance.id}")
        else:
            # form wasn't valid, let them try again
            print("Form is invalid - Try again!")
            # send the form back to show the errors as well as repopulate with the data they entered
            return render(request, f"/attorney/details/{attorney_id}", {"form": form})

    # Since this is not a post request, redirect them to the attorney list
    return redirect("/attorney/")
