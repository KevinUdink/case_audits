from django.shortcuts import render, redirect

# Create your views here.
def view_list(request):
    print("in attorney view_list")
    return render(request, "attorney_list.html")

def details(request, attorney_id):
    print("in attorney details")
    # Get the attorney that matches this id
    attorney = {
        "id": 6,
        "first_name": "Test",
        "last_name": "attorney",
        "manager_id": 3,
        "default_audit_type_id": 2,
        "active": False,
    }
    # Get the list of managers
    managers = [
        { "id": "1", "first_name": "Sally", "last_name": "Manager"},
        { "id": "2", "first_name": "Billy", "last_name": "Manager"},
        { "id": "3", "first_name": "Bob", "last_name": "Manager"},
        { "id": "4", "first_name": "Denyce", "last_name": "Manager"},
    ]
    # Get the list of default audit types
    audit_types = [
        { "id": "1", "name": "PTC" },
        { "id": "2", "name": "DV" },
        { "id": "3", "name": "DUI" },
    ]
    context = {
        "is_add_attorney": False,
        "attorney": attorney,
        "managers": managers,
        "audit_types": audit_types,
    }
    return render(request, "attorney_details.html", context)

def add(request):
    print("in attorney add")
    # using blank values to simplify the HTML page we will render
    attorney = {
        "id": 5,
        "first_name": "",
        "last_name": "",
        "manager_id": 0,
        "default_audit_type_id": 0,
        "active": True,
    }
    # Get the list of managers
    managers = [
        { "id": "1", "first_name": "Sally", "last_name": "Manager"},
        { "id": "2", "first_name": "Billy", "last_name": "Manager"},
        { "id": "3", "first_name": "Bob", "last_name": "Manager"},
        { "id": "4", "first_name": "Denyce", "last_name": "Manager"},
    ]
    # Get the list of default audit types
    audit_types = [
        { "id": "1", "name": "PTC" },
        { "id": "2", "name": "DV" },
        { "id": "3", "name": "DUI" },
    ]
    context = {
        "is_add_attorney": True,
        "attorney": attorney,
        "managers": managers,
        "audit_types": audit_types,
    }
    return render(request, "attorney_details.html", context)

def create(request):
    print("in attorney create")
    print("\tFirst name:", request.POST['first_name'])
    print("\tLast name:", request.POST['last_name'])
    print("\tManager ID:", request.POST['manager'])
    print("\tAudit Type ID:", request.POST['audit_type'])
    if "is_active" in request.POST:
        print("\tActive:", request.POST['is_active'])
    attorney_id = 9
    return redirect(f"/attorney/details/{attorney_id}")

# update the attorney object and save to DB
def update(request, attorney_id):
    print("in attorney update")
    print("\tFirst name:", request.POST['first_name'])
    print("\tLast name:", request.POST['last_name'])
    print("\tManager ID:", request.POST['manager'])
    print("\tAudit Type ID:", request.POST['audit_type'])
    if "is_active" in request.POST:
        print("\tActive:", request.POST['is_active'])
    return redirect(f"/attorney/details/{attorney_id}")
