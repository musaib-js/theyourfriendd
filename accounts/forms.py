from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import Patient, User, Consultant

class PatientSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        patient = Patient.objects.create(user=user)
        patient.save()
        return user

class ConsultantSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
        consultant = Consultant.objects.create(user=user)
        consultant.save()
        return user

class PatientForm(forms.ModelForm):  
    class Meta:  
        model = Patient
        fields = ['name', 'age', 'gender', 'history']

# class PatientForm(forms.Form):
#     subject = forms.CharField(max_length=100)
#     message = forms.CharField(widget=forms.Textarea)
#     sender = forms.EmailField()
#     cc_myself = forms.BooleanField(required=False) 

class ConsultantForm(forms.ModelForm):  
    class Meta:  
        model = Consultant
        fields = ['name', 'qualification', 'speciality', 'clinic', 'contact', 'email', 'photo', 'bio'] 