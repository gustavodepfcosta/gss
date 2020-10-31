from django.urls import path
from .views import *


urlpatterns = [
    path(
        '', 
        index, 
        name='index.html',
        ),

    path(
        'registrations/', 
        registrations, 
        name='registrations.html',
        ),

    path(
        'registrations/new-professor/',
        new_professor, 
        name='new-professor.html',
        ),

    path(
        'registrations/new-student/', 
        new_student, 
        name='new-student.html',
        ),

    path(
        'registrations/new-guardian/', 
        new_guardian, 
        name='new-guardian.html',
        ),

    path(
        'registrations/new-subject/', 
        new_subject, 
        name='new-subject.html',
        ),

    path(
        'grades-menu/', 
        grades_menu, 
        name='grades-menu.html',
        ),

    path(
        'grades-menu/grades-manager/', 
        grades_manager, 
        name='grades-manager.html',
        ),
        
    path(
        'contact/', 
        contact, 
        name="contact.html",
        ),
]