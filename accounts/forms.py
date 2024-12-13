from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
from django.core.exceptions import ValidationError

class RegisterForm(UserCreationForm):
    firstname = forms.CharField(max_length=255, label="First Name")
    lastname = forms.CharField(max_length=255, label="Last Name")
    phone_number = forms.CharField(max_length=15, required=False, label="Phone Number")
    email = forms.EmailField(required=True, label="Email")
    address = forms.CharField(widget=forms.Textarea, required=False, label="Address")

    class Meta:
        model = User
        fields = ['password1', 'password2']  # Removed 'username' from here

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['firstname']  # Set username to firstname
        if commit:
            user.save()
            UserProfile.objects.create(
                user=user,  # Link to the user
                firstname=self.cleaned_data['firstname'],
                lastname=self.cleaned_data['lastname'],
                phone_number=self.cleaned_data['phone_number'],
                email=self.cleaned_data['email'],
                address=self.cleaned_data['address']
            )
        return user

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("A user with that email already exists.")
        return email
