from .models import Attorney
from manager_app.models import Manager
from django import forms
# import datetime

class AttorneyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AttorneyForm, self).__init__(*args, **kwargs)

        # adding a form control class to each form input to enable bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = Attorney 

        # empty_label could also include my own custom test as a default selected value, but
        #   I am choosing "None" to prevent us from selecting an invalid manager
        managers_field = forms.ModelChoiceField(queryset=Manager.objects.all(), empty_label=None)
        
        # include only 3 fields that exist in the Attorney Model to create form controls
        fields = ("first_name", "last_name", managers_field)

