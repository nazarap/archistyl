# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class Subtype(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    styles = models.ManyToManyField(Style)


class Style(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    subtypes = models.ManyToManyField(Subtype)


class SubtypeImage(models.Model):
    image = models.ImageField(upload_to='images')
    subtype = models.ForeignKey(Subtype, on_delete=models.CASCADE)


class StyleImage(models.Model):
    image = models.ImageField(upload_to='images')
    style = models.ForeignKey(Style, on_delete=models.CASCADE)


class SubtypeStyle(models.Model):
    subtype = models.ForeignKey(Subtype, on_delete=models.CASCADE)
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
