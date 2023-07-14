from django import forms
from django.forms import ModelForm
from .models import Therapist,Patient,Device,Maintenance,Damage,Treatment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PatientForm(forms.ModelForm):
    class Meta:
        model= Patient
        fields = '__all__'
        
        gender=[('male','male'),
            ('female','female')]
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'Id':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            'date_of_birth':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'gender':forms.Select(attrs={'class':'form-control','choices':'gender'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'Responsible_party':forms.TextInput(attrs={'class':'form-control'}),
            'height':forms.TextInput(attrs={'class':'form-control'}),
            'weight':forms.TextInput(attrs={'class':'form-control'}),
            'integrated_doctors':forms.Textarea(attrs={'class':'form-control'}),
            'surgical':forms.Textarea(attrs={'class':'form-control'}),
            'primary_diagnosis':forms.Textarea(attrs={'class':'form-control'}),
        }

        

class TherapistForm(ModelForm):
    class Meta:
        model=Therapist
        fields = "__all__"
        
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'id':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            'date_of_birth':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'gender':forms.Select(attrs={'class':'form-control','choices':'gender'}),
            'phone':forms.TextInput(attrs={'class':'form-control',}),
            'university':forms.TextInput(attrs={'class':'form-control'}),
            'degree':forms.TextInput(attrs={'class':'form-control'}),
            'specialty':forms.TextInput(attrs={'class':'form-control'}),
           
        }

class DeviceForm(ModelForm):
    class Meta:
        model=Device
        fields = "__all__"
        
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'deviceid':forms.TextInput(attrs={'class':'form-control'}),
            'production_date':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'period_of_guarantee':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'country_of_manfucature':forms.TextInput(attrs={'class':'form-control'}),
            'company_of_manfucature':forms.TextInput(attrs={'class':'form-control'}),
            'duration_per_session':forms.NumberInput(attrs={'class':'form-control'}),
            'Max_number_per_day':forms.NumberInput(attrs={'class':'form-control'}),
            'agent':forms.TextInput(attrs={'class':'form-control'}),
            'usage_per_day':forms.NumberInput(attrs={'class':'form-control'}),
            'department':forms.TextInput(attrs={'class':'form-control'}),
            'model':forms.TextInput(attrs={'class':'form-control'}),
            'brand':forms.TextInput(attrs={'class':'form-control'}),
            'quantity':forms.NumberInput(attrs={'class':'form-control'}),
           
        }

class MaintenanceForm(ModelForm):
    class Meta:
        model=Maintenance
        fields = "__all__"

        choices=[('yes','yes'),
             ('no','no')]
        widgets={
            'clinic':forms.TextInput(attrs={'class':'form-control'}),
            'date_of_supply':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            #'name':forms.TextInput(attrs={'class':'form-control'}),
            'country':forms.TextInput(attrs={'class':'form-control'}),
            'model':forms.TextInput(attrs={'class':'form-control'}),
            'agent':forms.TextInput(attrs={'class':'form-control'}),
            'serial':forms.TextInput(attrs={'class':'form-control'}),
            'company':forms.TextInput(attrs={'class':'form-control'}),
            'date':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'Eng_signature':forms.TextInput(attrs={'class':'form-control'}),
            'Company_signature':forms.TextInput(attrs={'class':'form-control'}),
            'device_codition':forms.Select(attrs={'class':'form-control','choices':'choices'}),
            'notes':forms.Textarea(attrs={'class':'form-control'}),   
        }

class DamageForm(forms.ModelForm):
    class Meta:
        model=Damage
        fields = "__all__"

        widgets={
            'id':forms.TextInput(attrs={'class':'form-control'}),

            #'Devicess':forms.TextInput(attrs={'class':'form-control'}),
            'damage_date':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'damage_reason':forms.TextInput(attrs={'class':'form-control'}),
            'report_date':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'check_notes':forms.Textarea(attrs={'class':'form-control'}),
            'Examination_officer_name':forms.TextInput(attrs={'class':'form-control'}),
            'nurse_name':forms.TextInput(attrs={'class':'form-control'}), 
        }

class TreatmentForm(ModelForm):
    class Meta:
        model=Treatment
        fields = "__all__"
        
        widgets={
            'Patient_name':forms.TextInput(attrs={'class':'form-control'}),
            'id':forms.TextInput(attrs={'class':'form-control'}),
            'sessions':forms.TextInput(attrs={'class':'form-control'}),
            'date':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'signature':forms.TextInput(attrs={'class':'form-control'}),
            'notes':forms.Textarea(attrs={'class':'form-control'}),
           
        }

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'password1', 
            'password2', 
            ]
       
   
   


