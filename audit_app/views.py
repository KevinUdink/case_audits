from django.shortcuts import render, redirect

# Create your views here.
def view_list(request):
    print("in audit view_list")
    return render(request, "audit_list.html")

def details(request, audit_id):
    print("in audit details")
    # Get the audit that matches this id
    audit = {
        "id": 6,
        "name": "Test Audit",
        "desc": "DV audit",
        "active": False,
    }
    context = {
        "is_add_audit": False,
        "audit": audit,
    }
    return render(request, "audit_details.html", context)

def add(request):
    print("in audit add")
    # using blank values to simplify the HTML page we will render
    audit = {
        "id": 5,
        "name": "",
        "desc": "",
        "active": True,
    }
    context = {
        "is_add_audit": True,
        "audit": audit,
    }
    return render(request, "audit_details.html", context)

def create(request):
    print("in audit create")
    audit_id = 9
    return redirect(f"/audit/details/{audit_id}")

# update the audit object and save to DB
def update(request, audit_id):
    print("in audit update")
    return redirect(f"/audit/details/{audit_id}")
