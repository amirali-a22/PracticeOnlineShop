from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from accounts.models import User


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'full_name')

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise ValidationError("Passwords must match")
        return confirm_password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'full_name', 'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]


class LoginUserForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': "form-control",
        'placeholder': 'Your email'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control",
        'placeholder': 'Your Password'
    }))


class RegisterUserForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': "form-control",
        'placeholder': 'Your email'
    }))
    fullname = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Your fullname'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control",
        'placeholder': 'Your Password'
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control",
        'placeholder': 'Your confirm Password'
    }))

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email)
        if user.exists():
            raise forms.ValidationError('This Email Taken before')
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']
        if password and confirm_password:
            if confirm_password != password:
                raise forms.ValidationError('Your passwords does not match')
