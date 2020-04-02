from .models import AuditType, AuditCriteria
from django import forms
from django.forms import ModelForm, modelformset_factory, BaseModelFormSet


class AuditTypeForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(AuditTypeForm, self).__init__(*args, **kwargs)

        # adding form controls so we can easily add bootstrap classes to fields
        for name in self.fields.keys():
            if name == "is_current":
                self.fields[name].widget.attrs.update({
                    "class": "col-sm-1",
                    "style": "width:20px;height:20px",
                })
            else:
                self.fields[name].widget.attrs.update({
                    "class": "form-control col-sm-8",
                })

    class Meta:
        model = AuditType
        # all of the criteria will be objects created in the view.py
        fields = ("name", "desc", "is_current")
        labels = {
            "desc": "Description",
        }
        # help_texts = {
        #     "desc": "This will help identify what this audit is about",
        # }
        widgets = {
            "desc": forms.TextInput(),
        }

class AuditCriteriaForm(ModelForm):

    class Meta:
        model = AuditCriteria
        # all of the criteria will be objects created in the view.py
        fields = ("question", "max_points")
        labels = {
            "max_points": "Max Points",
        }
        # help_texts = {
        #     "desc": "This will help identify what this audit is about",
        # }
        widgets = {
            "question": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Enter question / criteria here",
                "cols": 10,   # this is overridden using CSS to use 100% of the space
                "rows": 4
                }
            ),
            "max_points": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "style": "min-width: 100px;",   # use 6 character width to allow for arrows on the side
                    "min": "1",
                    "max": "10",
                }
            ),
        }

# formsets allow us to create multiple forms of the same type in our html template
AuditCriteriaFormset = modelformset_factory(
    AuditCriteria,
    fields=("question", "max_points", ),
    form=AuditCriteriaForm,
)
