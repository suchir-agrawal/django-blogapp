from django import forms


class Login(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=50,widget=forms.PasswordInput)


class Signup(forms.Form):
    firstname = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'Enter your firstname'}))
    lastname = forms.CharField(max_length=40)
    username = forms.CharField(max_length=40)
    email = forms.EmailField()
    password = forms.CharField(max_length=50,widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=50,widget=forms.PasswordInput)
    pic = forms.ImageField()

