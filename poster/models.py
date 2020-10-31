from django.db import models
from django.db.models import signals
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey
from django.template.defaultfilters import slugify
from stdimage.models import StdImageField
from datetime import datetime
from django.utils import timezone


class BaseModel(models.Model):
    created = models.DateField('Created', auto_now_add=True)
    modified = models.DateField('Modified', auto_now=True)
    active = models.DateTimeField('Active', default=timezone.now())

    class Meta:
        abstract = True


class Professor(BaseModel):
    first_name = models.CharField('First Name', max_length=50)
    last_name = models.CharField('Last Name', max_length=50)
    email = models.EmailField('e-mail', max_length=100)
    graduation = models.CharField('Graduation', max_length=100)
    phone_number = models.IntegerField('Phone Number')

    def __str__(self) -> str:
        return f'{self.first_name} - {self.graduation}'


class Student(BaseModel):
    first_name = models.CharField('First Name', max_length=50)
    last_name = models.CharField('Last Name', max_length=50)
    age = models.IntegerField('Age')

    def __str__(self) -> str:
        return f'{self.first_name} - {self.last_name}'


class Guardian(BaseModel):
    first_name = models.CharField('First Name', max_length=50)
    last_name = models.CharField('Last Name', max_length=50)
    email = models.EmailField('e-mail', max_length=100)
    phone_number = models.IntegerField('Phone Number')
    address = models.CharField('Address', max_length=100)

    def __str__(self) -> str:
        return f'{self.first_name} - {self.last_name}'


class Subject(BaseModel):
    subject_name = models.CharField('Subject Name', max_length=80)
    year = models.IntegerField('Year')
    professor_id = ForeignKey(Professor, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f'{self.subject_name} - year: {self.year}'


class Contact(BaseModel):
    first_name = models.CharField('First Name', max_length=50)
    last_name = models.CharField('Last Name', max_length=50)
    email = models.EmailField('e-mail', max_length=100)
    phone_number = models.IntegerField('Phone Number')
    subject = models.CharField('Subject', max_length=100)
    message = models.TextField('Message')


def professor_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.first_name)

def student_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.last_name)

def guardian_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.last_name)

def subject_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.last_name)


signals.pre_save.connect(professor_pre_save, sender=Professor)
signals.pre_save.connect(student_pre_save, sender=Student)
signals.pre_save.connect(guardian_pre_save, sender=Guardian)
signals.pre_save.connect(subject_pre_save, sender=Subject)
