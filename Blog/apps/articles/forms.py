from django import forms
# from django.contrib.auth.models import User
from .models import Articles
from apps.users.models  import CustomUser



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username','first_name','email','password','password2')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password']   != cd['password2']:
            raise forms.ValidationError('password doesnot match')
        return cd['password2']


class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ('title','description')


class ArticleUpdateForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ('title','description')



