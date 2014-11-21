from django.db import models
from django.utils.translation import ugettext_lazy as _


class Department(models.Model):

    name = models.CharField(_(u'Name'), max_length=255)
    building = models.CharField(_(u'Building'), max_length=255)
    address = models.CharField(_(u'Address'), max_length=255)

    def __unicode__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(_(u'Name'), max_length=255)
    department = models.ForeignKey(Department)
    capacity = models.IntegerField(_(u'Capacity'))

    def __unicode__(self):
        return self.name