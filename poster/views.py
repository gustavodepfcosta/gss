from django.contrib.messages.api import error
from django.http.request import RAISE_ERROR
from poster.forms import *
from django.shortcuts import render
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def registrations(request):
    return render(request, 'registrations.html')


def enrollments(request):
    context = {}

    return render(request, 'enrollments.html', context)


def new_student(request):
    form = StudentModelForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.save()

            messages.success(request, 'New student registered successfully')
            form = StudentModelForm()

        else:
            messages.error(request, 'Oops! Something went wrong. Please, try again later.')

    else:
        form = StudentModelForm()

    context = {
        'form': form,
    }

    return render(request, 'new-student.html', context)


def new_guardian(request):
    form = GuardianModelForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.save()

            messages.success(request, 'New guardian registered successfully')
            form = GuardianModelForm

        else:
            messages.error(request, 'Oops! Something went wrong. Please, try again later.')
        
    else:
        form = GuardianModelForm()

    context = {
        'form': form,
    }

    return render(request, 'new-guardian.html', context)


def new_subject(request):
    form = SubjectModelForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.save()

            messages.success(request, 'New Subject registered successfully')
            form = SubjectModelForm()

        else:
            messages.error(request, 'Oops! Something went wrong. Please, try again later.')

    else:
        form = SubjectModelForm()

    context = {
        'form': form
    }

    return render(request, 'new-subject.html', context)


def grades_menu(request):

    context = {
        'subjects': Subject.objects.all(),
    }

    return render(request, 'grades-menu.html', context)
 

def grades_manager(request):

    return render(request, 'grades-manager.html')


def new_professor(request):
    form = ProfessorModelForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.save()

            messages.success(request, 'New professor registered successfully!')
            form = ProfessorModelForm()

        else:
            messages.error(request, 'Oops! Something went wrong. Please, try again later!')
            
    else:
        form = ProfessorModelForm()

    context = {
        'form': form,
    }

    return render(request, 'new-professor.html', context)


def contact(request):
    form = ContactModelForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.save()
            form.send_mail()

            messages.success(request, 'Message sent successfully')
            form = ContactModelForm()

        else:
            messages.error(request, 'Oops! Something went wrong. Please, try again later.')
            
    else:
        form = ContactModelForm()

    context = {
        'form': form,
    }

    return render(request, 'contact.html', context)
