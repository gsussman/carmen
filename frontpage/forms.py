from django import forms

#http://stackoverflow.com/questions/12303478/how-to-customize-user-profile-when-using-django-allauth

class CustomSignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='First name', widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, label='Last name', widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()