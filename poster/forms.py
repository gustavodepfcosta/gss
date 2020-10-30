from django import forms
from .models import *


class ProfessorModelForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = [
            'first_name',
            'last_name',
            'email',
            'graduation',
            'phone_number',
            'picture',
        ]


class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'age',
        ]


class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'subject',
            'message',
        ]
