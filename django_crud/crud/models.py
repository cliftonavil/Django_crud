from django.db import models
from django.urls import reverse
from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


from crud.choice import *


class Book(models.Model):
    name = models.CharField(max_length=200,)
    author = models.CharField(max_length=50)
    price = models.IntegerField()
    publish_year = models.IntegerField()
    pages = models.IntegerField()
    # status = models.CharField(max_length=20)
    status = models.CharField(choices=book_status,max_length=20, default='Available')


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('CRUD:book_edit', kwargs={'pk': self.pk})

    #year validation
    def validate_year(self):
        if self.publish_year < 1990 and self.publish_year > 2018:
            raise ValidationError(
                _('%(publish_year) Not a Valid Year  1990 - 2018'),
                params={'publish_year': publish_year},
            )


