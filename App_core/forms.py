from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter your username',
        'class':'w-full py-4 px-6 rounded-xl',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'your password',
        'class':'w-full py-4 px-6 rounded-xl',
    }))
    
# class SignupForm(UserCreationForm):

#     class Meta:
#         model = User  # Replace YourUserModel with the actual user model you are using
#         fields = ('username', 'email', 'password1', 'password2')  # Specify the fields you want in the form
    
#     username = forms.CharFiled(widget=forms.TextInput(attrs={
#         'placeholder': 'Your username',
#     }))
    
    


class SignupForm(UserCreationForm):
    # additional form fields if needed
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter your username',
        'class':'w-full py-4 px-6 rounded-xl',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Enter your email',
        'class':'w-full py-4 px-6 rounded-xl',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'your password',
        'class':'w-full py-4 px-6 rounded-xl',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Reppeat password',
        'class':'w-full py-4 px-6 rounded-xl',
    }))
    # Add other fields as needed

    class Meta:
        model = User  # Replace YourUserModel with the actual user model you are using
        fields = ('username', 'email', 'password1', 'password2')
