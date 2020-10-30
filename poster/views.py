from django.contrib.messages.api import error
from django.http.request import RAISE_ERROR
from poster.forms import *
from django.shortcuts import render
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def registrations(request):
    return render(request, 'registrations.html')


def new_student(request):
    form = StudentModelForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_Data['age']

            print(first_name)
            print(last_name)
            print(age)

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
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            address = form.cleaned_data['address']

            messages.success(request, 'New guardian registered successfully')
            form = GuardianModelForm

        else:
            messages.error(request, 'Oops! Something went wrong. Please, try again later.')
        
    else:
        form = GuardianModelForm

    context = {
        'form': form,
    }

    return render(request, 'new-guardian.html', context)
    

def new_professor(request):
    form = ProfessorModelForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            graduation = form.cleaned_data['graduation']
            phone_number = form.cleaned_data['phone_number']
            picture = form.cleaned_data['picture']


            print('Professor cadastrado com sucesso')
            print(f'First Name: {first_name}')
            print(f'Last Name: {last_name}')
            print(f'e-mail: {email}')
            print(f'Graduation: {graduation}')
            print(f'Phone Number: {phone_number}')
            print(f'Picture URL: {picture}')

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
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']


            print('Message sent successfully')
            print(f'First Name: {first_name}')
            print(f'Last Name: {last_name}')
            print(f'e-mail: {email}')
            print(f'Phone Number: {phone_number}')
            print(f'Subject: {subject}')
            print(f'Message: {message}')

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
