from django.contrib import admin
from .models import *


@admin.register(Professor)
class NewProfessorAdmin(admin.ModelAdmin):
    pass
