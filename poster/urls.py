from django.urls import path
from .views import *


urlpatterns = [
    path(
        '', 
        IndexView.as_view(), 
        name='index.html',
        ),

    path(
        'registrations/', 
        RegistrationsView.as_view(), 
        name='registrations.html',
        ),

    path(
        'registrations/new-professor/',
        NewProfessorView.as_view(), 
        name='new-professor.html',
        ),

    path(
        'registrations/new-student/', 
        NewStudentView.as_view(), 
        name='new-student.html',
        ),

    path(
        'registrations/new-guardian/', 
        NewGuardianView.as_view(), 
        name='new-guardian.html',
        ),

    path(
        'registrations/new-subject/', 
        NewSubjectView.as_view(), 
        name='new-subject.html',
        ),

    path(
        'grades-manager/', 
        GradesManagerView.as_view(), 
        name='grades-manager.html',
        ),
        
    path(
        'contact/', 
        ContactView.as_view(), 
        name="contact.html",
        ),

    path(
        'enrollments/',
        EnrollmentsView.as_view(),
        name='enrollments.html',
    ),

    path(
        'subscriptions-menu/',
        SubscriptionsMenuView.as_view(),
        name='subscriptions-menu.html',
    ),

    path(
        'student-guardian-menu/',
        StudentsGuardiansMenuView.as_view(),
        name='student-guardian-menu.html',
    ),
]
