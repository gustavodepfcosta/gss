from django.contrib.messages.api import error
from poster.forms import *
from django.shortcuts import render
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def registrations(request):
    return render(request, 'registrations.html')


def subscriptions_menu(request):
    form = SubscriptionsModelForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.save()

            messages.success(request, 'Done!')
            form = SubscriptionsModelForm()

        else:
            messages.error(request, 'Oops! Something went wrong.')

    else:
        form = SubscriptionsModelForm()

    context = {
        'form': form,
    }

    return render(request, 'subscriptions-menu.html', context)


def students_guardians_menu(request):
    form = StudentGuardianForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.save()

            messages.success(request, 'Done!')
            form = StudentGuardianForm()

        else:
            messages.error(request, 'Oops! Something went wrong.')

    else:
        form = StudentGuardianForm()

    context = {
        'form': form,
    }
            
    return render(request, 'student-guardian-menu.html', context)


def enrollments(request):
    return render(request, 'enrollments.html')


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
 

def grades_manager(request):
    form = GradesForm()

    if str(request.method) == 'POST':   
        if form.is_valid():
            form.save()

            messages.success(request, 'Grades assigned successfully')
            form = GradesForm()

        else:
            messages.error(request, 'Oops! Somethig went worng. Please, try again later!')

    else:
        form = GradesForm()

    context = {
        'form': form,
    }

    return render(request, 'grades-manager.html', context)


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
