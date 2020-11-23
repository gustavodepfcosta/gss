from django import forms
from .models import *
from django.core.mail.message import EmailMessage


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


class SubscriptionsModelForm(forms.ModelForm):
    student_id = forms.ModelChoiceField(queryset=Student.objects.all(), initial=0, label='To which student would you like to assign a subject?')
    subject_id = forms.ModelChoiceField(queryset=Subject.objects.all(), initial=0, label='Which subject?')
    
    class Meta:
        model = Subscriptions
        fields = [
            'student_id',
            'subject_id',
        ]


class StudentGuardianForm(forms.ModelForm):
    student_id = forms.ModelChoiceField(queryset=Student.objects.all(), initial=0, label='To which student would you like to assign a guardian?')
    guardian_id = forms.ModelChoiceField(queryset=Guardian.objects.all(), initial=0, label='Which guardian?')
    
    class Meta:
        model = GuardianStudentBridge
        fields = [
            'student_id',
            'guardian_id',
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

    def send_mail(self):
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_ name']
        email = self.cleaned_data['email']
        phone_number = self.cleaned_data['phone_number']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']

        content = f'Name: {first_name} {last_name}\ne-mail: {email}\nPhone Number: {phone_number}\nSubject: {subject}\nMessage: {message}'

        mail = EmailMessage(
            subject='e-mail sent by automatized django system',
            body=content,
            to=['contact@yourdomain.com'],
            from_email=['contact@yourdomain.com'],
            headers={'reply-to': email},
        )

        mail.send()
        