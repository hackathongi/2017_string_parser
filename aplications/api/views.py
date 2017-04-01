from django.http import HttpResponse
from django.shortcuts import render
import urllib2

from aplications.devices.models import Device


# Repite el texto enviado
def echo(request, text):
    return HttpResponse(text)


# Repite el texto enviado
def parse(request, text):
    return HttpResponse(text)
