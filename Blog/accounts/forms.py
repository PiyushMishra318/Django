from django import forms
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class StatusUpdate(forms.Form):
    Body = forms.CharField(label='Post')
    Posted_on = forms.DateField()

class CommentForm(forms.Form):
    text = forms.CharField()
    Posted_on = forms.DateField()

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=(
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2'
        )
        def save():
            user = super(RegistrationForm).save(commit=False)
            user.first_name = user.cleaned_data['first_name']
            user.last_name = user.cleaned_data['last_name']

            if commit:
                user.save()
            return user
