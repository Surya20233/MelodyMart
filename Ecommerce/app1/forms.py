from django import forms
from app1.models import Coustomer_Details

class CustomerDetailsForm(forms.ModelForm):
    class Meta:
        model = Coustomer_Details
        fields = ['user', 'name', 'mobile','category', 'address', 'city','pincode', 'state','country']
        
        exclude = ['user']  

        widgets = {
            'Address': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Mobile Number'}),
            'address': forms.TextInput(attrs={'class': 'form-control',  'placeholder': 'Enter Building Number,Street Name & Locality'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter City'}),
            'pincode':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Postalcode'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter State'}),
            'country': forms.HiddenInput(),  
        }

    