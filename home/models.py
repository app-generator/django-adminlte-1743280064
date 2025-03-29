# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Testtest(models.Model):

    #__Testtest_FIELDS__
    test1 = models.CharField(max_length=255, null=True, blank=True)
    test2 = models.TextField(max_length=255, null=True, blank=True)
    test3 = models.BooleanField()
    test4 = models.IntegerField(null=True, blank=True)
    test5 = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Testtest_FIELDS__END

    class Meta:
        verbose_name        = _("Testtest")
        verbose_name_plural = _("Testtest")



#__MODELS__END
