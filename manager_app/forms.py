from .models import Manager
from django import forms
# import datetime

class ManagerForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ManagerForm, self).__init__(*args, **kwargs)

        # adding a form control class to each form input to enable bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = Manager
        
        # include only 3 fields that exist in the Manager Model to create form controls
        fields = ("first_name", "last_name", "title")


class ManagerDetailsForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ManagerDetailsForm, self).__init__(*args, **kwargs)

        # adding a form control class to each form input to enable bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = Manager
        
        # include only 3 fields that exist in the Manager Model to create form controls
        fields = ("first_name", "last_name", "title", "is_active")

