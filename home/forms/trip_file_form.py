from django import forms
from home.models import TripFile


class TripFileForm(forms.ModelForm):
    class Meta:
        model = TripFile
        fields = ["file"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
