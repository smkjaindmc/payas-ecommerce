from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model
)
from django.contrib import messages
User=get_user_model()
class UserLoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'id':'email','placeholder':'User name'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'id':'password','placeholder':'Password'}))
    def clean(self,*args,**kwargs):
        username=self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')
        if username and password:
            user=authenticate(username=username,password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(UserLoginForm,self).clean(*args,**kwargs)        
                
                
class RegisterForms(forms.ModelForm):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'input','placeholder':'User name'}))
    password=forms.CharField(min_length=6,widget=forms.PasswordInput(attrs={'class': 'input','placeholder':'Password'}))
    email=forms.CharField(max_length=100,widget=forms.EmailInput(attrs={'class': 'input','placeholder':'Email'}))
    class Meta:
        model=User
        fields=[
            'username',
            'email',
            'password'
        ]
    def clean_email(self):
        email=self.cleaned_data.get('email')
        email_qs=User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email is already being used")
        return email    
    