from django.contrib.messages.api import error, success
from django.views.generic.edit import FormView
from poster.forms import *
from django.shortcuts import render
from django.contrib import messages
from django.views.generic import TemplateView, CreateView


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['subjects'] = Subject.objects.all()
        context['professors'] = Professor.objects.all()

        return context

class RegistrationsView(TemplateView):
    template_name = 'registrations.html'

class SubscriptionsMenuView(FormView):
    template_name = 'subscriptions-menu.html'
    model = Subscriptions
    form_class = SubscriptionsModelForm
    success_url = '/subscriptions-menu/'

    def form_valid(self, form):
        return super().form_valid(form)

class StudentsGuardiansMenuView(FormView):
    template_name = 'student-guardian-menu.html'
    model = GuardianStudentBridge
    form_class = StudentGuardianForm

class EnrollmentsView(TemplateView):
    template_name = 'enrollments.html'

class NewStudentView(FormView):
    template_name = 'new-student.html'
    model = Student
    form_class = StudentModelForm
    success_url = '/registrations/new-student/'

    def form_valid(self, form):
        return super().form_valid(form)


class StudentBoardView(TemplateView):
    template_name = 'student-board.html'

    def get_context_data(self, **kwargs):
        context = super(StudentBoardView, self).get_context_data(**kwargs)
        context['students'] = Student.objects.all()

        return context

class NewGuardianView(FormView):
    template_name = 'new-guardian.html'
    model = Guardian
    form_class = GuardianModelForm
    success_url = '/registrations/new-guardian/'

    def form_valid(self, form):
        return super().form_valid(form)

class GuardianBoardView(TemplateView):
    template_name = 'guardian-board.html'

    def get_context_data(self, **kwargs):
        context = super(GuardianBoardView, self).get_context_data(**kwargs)
        context['guardians'] = Guardian.objects.all()

        return context

class NewSubjectView(FormView):
    template_name = 'new-subject.html'
    model = Subject
    form_class = SubjectModelForm
    success_url = '/registrations/new-subject/'

    def form_valid(self, form):
        return super().form_valid(form)

class SubjectBoardView(TemplateView):
    template_name = 'subject-board.html'

    def get_context_data(self, **kwargs):
        context = super(SubjectBoardView, self).get_context_data(**kwargs)
        context['subjects'] = Subject.objects.all()

        return context

class NewProfessorView(FormView):
    template_name = 'new-professor.html'
    model = Professor
    form_class = ProfessorModelForm
    success_url = '/registrations/new-professor/'

    def form_valid(self, form):
        return super().form_valid(form)

class ProfessorBoardView(TemplateView):
    template_name = 'professor-board.html'

    def get_context_data(self, **kwargs):
        context = super(ProfessorBoardView, self).get_context_data(**kwargs)
        context['professors'] = Professor.objects.all()

        return context


class GradesManagerView(FormView):
    template_name = 'grades-manager.html'
    model = Grades
    form_class = GradesForm
    success_url = '/grades-manager/'

    def form_valid(self, form):
        return super().form_valid(form)

class ContactView(FormView):
    template_name = 'contact.html'
    model = Contact
    form_class = ContactModelForm
    success_url = '/contact/'

    def form_valid(self, form):
        # form.send_mail()
        return super().form_valid(form)
