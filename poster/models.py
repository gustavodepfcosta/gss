from django.db import models
from django.db.models import signals
from django.db.models.fields import CharField
from django.template.defaultfilters import slugify
from datetime import datetime
from django.utils import timezone
from stdimage.models import StdImageField
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
    picture = StdImageField('Picture', upload_to='product', variations={'thumb': (124, 124)})

    def __str__(self) -> str:
        return f'{self.first_name} - {self.graduation}'


def professor_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.first_name)


class Student(BaseModel):
    first_name = models.CharField('First Name', max_length=50)
    last_name = models.CharField('Last Name', max_length=50)
    age = models.IntegerField('Age')

    def __str__(self) -> str:
        return f'{self.first_name} - {self.last_name}'


def student_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.first_name)


class Contact(BaseModel):
    first_name = models.CharField('First Name', max_length=50)
    last_name = models.CharField('Last Name', max_length=50)
    email = models.EmailField('e-mail', max_length=100)
    phone_number = models.IntegerField('Phone Number')
    subject = models.CharField('Subject', max_length=100)
    message = models.TextField('Message')


signals.pre_save.connect(professor_pre_save, sender=Professor)
signals.pre_save.connect(student_pre_save, sender=Student)
