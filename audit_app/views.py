from django.shortcuts import render, redirect
from .models import AuditType, AuditCriteria
from .forms import AuditTypeForm, AuditCriteriaFormset #, AuditCriteriaFilteredFormset #, AuditCriteriaFormset
from django.forms import modelformset_factory #, BaseModelFormSet

# Create your views here.
def view_list(request):
    print("\nIn audit view_list")
    audits = AuditType.objects.all()
    print(f"audits: {audits}")
    context = {
        "audits": audits,
    }
    return render(request, "audit_list.html", context)

def details(request, audit_id):
    print("\nIn audit details")
    # Get the audit and criteria that matches this id
    audit_type = AuditType.objects.get(id=audit_id)
    atForm = AuditTypeForm(instance=audit_type)

    # populate the set with the data specific to this audit
    #   ignore the error related to queryset not being a valid option
    acFormset = AuditCriteriaFormset(
        queryset=AuditCriteria.objects.filter(audit_type=audit_type), 
    )
    # print("ac formset:", acFormset)

    context = {
        "is_add_audit": False,
        "is_update_audit": False,
        "atForm": atForm,
        "acFormset": acFormset,
    }
    return render(request, "audit_details.html", context)

def add(request):
    print("\nIn audit add")

    # using blank values to populate the HTML page we will render
    atForm = AuditTypeForm()
    acFormset = AuditCriteriaFormset(
        queryset=AuditCriteria.objects.none(), 
    )

    context = {
        "is_add_audit": True,
        "is_update_audit": False,
        "atForm": atForm,
        "acFormset": acFormset,
    }
    return render(request, "audit_details.html", context)

def create(request):
    print("\nIn audit create")
    if request.method == "POST":
        audit_type_form = AuditTypeForm(request.POST)
        audit_criteria_formset = AuditCriteriaFormset(request.POST)
        
        if audit_type_form.is_valid() and audit_criteria_formset.is_valid():
            # first save the audit type so we can get the object back for the creation of the criteria entries
            audit = audit_type_form.save()

            for acForm in audit_criteria_formset:
                print(f"audit criteria object: {acForm}")
                print(f"cleaned data: {acForm.cleaned_data}")
                # The last criteria form is empty, skip it
                if "question" in acForm.cleaned_data:
                    # we need to create the object without saving it so we can add the audit type object
                    #    if we don't, the creation will fail since it needs the audit type object
                    criteria = acForm.save(commit=False)
                    criteria.audit_type = audit
                    criteria.save()
                # else:
                #     print('found form that is empty - this should be the last entry')
            
            # redirect to the audit details page
            return redirect(f"/audit/details/{audit.id}")
        else:
            print(f"something is invalid in one of the forms: {audit_type_form.errors} or {audit_criteria_formset.errors}")
            context = {
                "is_add_audit": True,
                "atForm": audit_type_form,
                "acFormset": audit_criteria_formset,
            }
            return render(request, "audit_details.html", context)
    
    # go back to the list if this wasn't an actual post request
    return redirect("/audit/")


# update the audit object and save to DB
def update(request, audit_id):
    print("\nIn audit update")
    return redirect(f"/audit/details/{audit_id}")
