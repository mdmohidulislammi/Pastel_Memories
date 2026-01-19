from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Memory


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "w-full px-4 py-3 rounded-xl  border border-purple-300 focus:outline-none focus:ring-2 focus:ring-purple-500 text-white",
            "placeholder": "First name"
        })
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "w-full px-4 py-3 rounded-xl border border-purple-300 focus:outline-none focus:ring-2 focus:ring-purple-500 text-white",
            "placeholder": "Last name"
        })
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "w-full px-4 py-3 rounded-xl border border-purple-300 focus:outline-none focus:ring-2 focus:ring-purple-500 text-white",
            "placeholder": "Username"
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "w-full px-4 py-3 rounded-xl border border-purple-300 focus:outline-none focus:ring-2 focus:ring-purple-500 text-white",
            "placeholder": "Email address"
        })
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            "class": "w-full px-4 py-3 rounded-xl border border-purple-300 focus:outline-none focus:ring-2 focus:ring-purple-500 text-white",
            "placeholder": "Password"
        })
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            "class": "w-full px-4 py-3 rounded-xl border border-purple-300 focus:outline-none focus:ring-2 focus:ring-purple-500 text-white",
            "placeholder": "Confirm Password"
        })
    )
    
    class Meta:
        model = User
        fields = ("first_name", "last_name","username", "email", "password1", "password2")
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username


class Update_User_Form(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "w-full px-4 py-3 rounded-xl  border border-purple-300 focus:outline-none focus:ring-2 focus:ring-purple-500 text-white",
            "placeholder": "First name"
        })
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "w-full px-4 py-3 rounded-xl border border-purple-300 focus:outline-none focus:ring-2 focus:ring-purple-500 text-white",
            "placeholder": "Last name"
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "w-full px-4 py-3 rounded-xl border border-purple-300 focus:outline-none focus:ring-2 focus:ring-purple-500 text-white",
            "placeholder": "Email address"
        })
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "w-full px-4 py-3 rounded-xl border border-purple-300 focus:outline-none focus:ring-2 focus:ring-purple-500 text-white",
            "placeholder": "Username"
        })
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            "class": "w-full px-4 py-3 rounded-xl border border-purple-300 focus:outline-none focus:ring-2 focus:ring-purple-500 text-white",
            "placeholder": "Password"
        })
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            "class": "w-full px-4 py-3 rounded-xl border border-purple-300 focus:outline-none focus:ring-2 focus:ring-purple-500 text-white",
            "placeholder": "Confirm Password"
        })
    
    )
    
    class Meta:
        model = User
        fields = ("first_name", "last_name","username", "email", "password1", "password2")
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username



class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "w-full px-4 py-3 rounded-xl border border-purple-300 focus:outline-none focus:ring-2 focus:ring-purple-500 text-black",
            "placeholder": "Username"
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "w-full px-4 py-3 rounded-xl border border-purple-300 focus:outline-none focus:ring-2 focus:ring-purple-500 text-black",
            "placeholder": "Password"
        })
    )
class MemoryForm(forms.ModelForm):
    title = forms.CharField(
        label="Memory Title",
        widget=forms.TextInput(attrs={
            "class": "w-full px-4 py-3 rounded-xl border border-purple-300 focus:outline-none focus:ring-2 focus:ring-purple-500 text-black",
            "placeholder": "Memory title"
        })
    )
    body = forms.CharField(
        label="Your Memory",
        widget=forms.Textarea(attrs={
            "class": "w-full px-4 py-3 rounded-xl border border-purple-300 focus:outline-none focus:ring-2 focus:ring-purple-500 resize-none text-black",
            "placeholder": "Write your memory here...",
            "rows": 8
        })
    )

    class Meta:
        model = Memory
        fields = ("title", "body")
