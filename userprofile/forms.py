from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Vendor
from django.contrib.auth.models import User
from django import forms
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            "bio",
            "location",
            "profile_picture",
        )
class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = (
            "identification",
            "image",
            "identification_number",
            "first_name",
            "last_name",
            "mobile_number",
            "bussiness_name",
            "bussiness_address",
            "bussiness_number",
        )