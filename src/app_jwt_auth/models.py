from django.db import models
from django.utils.translation import ugettext_lazy as _


class Product(models.Model):
    name = models.TextField(_('Product Name'), max_length=25)
    date = models.DateField(_("Date"), auto_now=True, auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return 

    def __unicode__(self):
        return 
