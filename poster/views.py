from django.contrib.messages.api import error, success
from poster.forms import *
from django.shortcuts import render
from django.contrib import messages
from django.views.generic import TemplateView, CreateView


class IndexView(TemplateView):
    template_name = 'index.html'


class RegistrationsView(TemplateView):
    template_name = 'registrations.html'


class SubscriptionsMenuView(CreateView):
    template_name = 'subscriptions-menu.html'
    model = Subscriptions
    form_class = SubscriptionsModelForm


class StudentsGuardiansMenuView(CreateView):
    template_name = 'student-guardian-menu.html'
    model = GuardianStudentBridge
    form_class = StudentGuardianForm


class EnrollmentsView(TemplateView):
    template_name = 'enrollments.html'


class NewStudentView(CreateView):
    template_name = 'new-student.html'
    model = Student
    form_class = StudentModelForm


class NewGuardianView(CreateView):
    template_name = 'new-guardian.html'
    model = Guardian
    form_class = GuardianModelForm


class NewSubjectView(CreateView):
    template_name = 'new-subject.html'
    model = Subject
    form_class = SubjectModelForm
 

class NewProfessorView(CreateView):
    template_name = 'new-professor.html'
    model = Professor
    form_class = ProfessorModelForm


class GradesManagerView(CreateView):
    template_name = 'grades-manager.html'
    model = Grades
    form_class = GradesForm


class ContactView(CreateView):
    template_name = 'contact.html'
    model = Contact
    form_class = ContactModelForm
