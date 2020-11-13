from django.forms import forms

class CsvUploadForm(forms.Form):

    file = forms.FileField()

