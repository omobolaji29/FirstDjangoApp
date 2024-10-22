from django.forms import ModelForm
# from .models import Customer
from django import forms


# class CustomerForm(ModelForm):
class CustomerForm(forms.Form):
     fullname= forms.CharField(max_length=50)
     age= forms.IntegerField()
     email=forms.EmailField()
     message =forms.CharField(widget=forms.Textarea)

    # class Meta:
    #     model = Customer
    #     fields = ('fullname',"age", 'email', 'telephone')