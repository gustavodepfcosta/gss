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


class GuardianModelForm(forms.ModelForm):
    class Meta:
        model = Guardian
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'address',
        ]

class SubjectModelForm(forms.ModelForm):
    professor_id = forms.ModelChoiceField(queryset=Professor.objects.all(), initial=0, label='Which Professor is responsible this subject?')

    class Meta:
        model = Subject
        fields = [
            'subject_name',
            'year',
            'professor_id',
        ]
        