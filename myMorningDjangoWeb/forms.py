from django import forms
# Define all the forms as classes


# This is a user registration form
class UserRegForm(forms.Form):
    # these are the input fields
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    password = forms.CharField(min_length=6)
