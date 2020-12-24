from django.contrib import admin
from .models import *


@admin.register(Professor)
class NewProfessorAdmin(admin.ModelAdmin):
    pass

@admin.register(Student)
class NewStudentAdmin(admin.ModelAdmin):
    pass

@admin.register(Guardian)
class NewGuardianAdmin(admin.ModelAdmin):
    pass

@admin.register(Subject)
class NewSubjectAdmin(admin.ModelAdmin):
    pass
