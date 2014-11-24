from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from administration.models import Department


class UserProfile(models.Model):   
    user = models.OneToOneField(User)

    name = models.CharField(_(u'Name'), max_length=255)
    date_of_birth = models.DateField(_(u'Date of birth'), blank=True, null=True)
    telephone = models.CharField(_(u'Telephone'), max_length=255)
    address = models.CharField(_(u'Address'), max_length=255)
    
    class Meta:
        abstract = True


class Doctor(UserProfile):

    department = models.ForeignKey(Department, null=True)
    head_of_department = models.BooleanField(_(u'Head of Department?'), default=False)

    class Meta:
        verbose_name = _('Doctor')
        verbose_name_plural = _('Doctors')
        ordering = ('name',)

    def __unicode__(self):
        return self.name


class Nurse(UserProfile):
    class Meta:
        verbose_name = _('Nurse')
        verbose_name_plural = _('Nurses')
        ordering = ('name',)

    def __unicode__(self):
        return self.name
