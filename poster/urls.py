from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index.html'),
    path('registrations/', registrations, name='registrations.html'),
    path('new-professor/', new_professor, name='new-professor.html'),
    path('new-student/', new_student, name='new-student.html'),
    path('new-guardian/', new_guardian, name='new-guardian.html'),
    path('new-subject/', new_subject, name='new-subject.html'),
    path('contact/', contact, name="contact.html"),
]