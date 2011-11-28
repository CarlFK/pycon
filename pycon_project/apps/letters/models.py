from django.db import models

from symposion.proposals.models import Proposal

class Country(models.Model):
    name = models.CharField(max_length=100)
    consulate_city = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name


