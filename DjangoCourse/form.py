from django import forms


class PostFormModel_Profile(forms.Form):
    username = forms.CharField(max_length=10,  initial='')
    password = forms.CharField(max_length=10,  initial='', widget=forms.PasswordInput)
    age      = forms.IntegerField()
    CHOICES = (('男', '男性',), ('女', '女性',))
    sex      = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    email    = forms.EmailField(max_length=50, initial='', required=False)
    order    = forms.CharField(max_length=10,  initial='', required=False, widget=forms.CheckboxInput)

