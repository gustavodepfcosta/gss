from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index.html'),
    path('registrations/', registrations, name='registrations.html'),
    path('new-professor/', new_professor, name='new-professor.html'),
    path('new-student', new_student, name='new-student.html'),
    path('contact/', contact, name="contact.html"),
]