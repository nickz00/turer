from django import forms
from .models import clients

class add_client(forms.Form):
    surname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required="")
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required="")
    lastname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required="")
    pas_num = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required="")
    pas_take = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required="")
    pas_reg = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required="")
    adress = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required="")
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required="")
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required="")
    activity = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required="")
    zp = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required="")
    tours = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required="")

class add_interested(forms.Form):
    surname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required="")
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required="")
    lastname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required="")
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required="")
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required="")
    comment = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required="")


class add_adver(forms.Form):
    for_person = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required="")
    text = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required="")
    response = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required="")
    date = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required="")