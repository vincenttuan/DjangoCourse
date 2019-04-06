from django import forms


class PostFormModel_Profile(forms.Form):
    username = forms.CharField(max_length=10, initial='')
    password = forms.CharField(max_length=10, initial='')
    age      = forms.IntegerField()
    sex      = forms.CharField(max_length=10,   initial='', required=False)
    email    = forms.EmailField(max_length=50,initial='', required=False)
    order    = forms.CharField(max_length=10, initial='', required=False)
