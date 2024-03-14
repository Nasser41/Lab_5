from django import forms

class Person(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password")