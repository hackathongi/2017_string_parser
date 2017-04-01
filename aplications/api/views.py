from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import urllib2
import json

from aplications.devices.models import Device
from aplications.devices.models import Action
from aplications.log.models import Log


# Repite el texto enviado
def echo(request, text):
    return HttpResponse(text)


# Repite el texto enviado
def parse(request, text):
    url_tarla = 'http://192.168.4.250/devices/{device}/cmds/{action}'
    devide_found = False
    text_split = text.split(',')
    test = '';

    for device in Device.objects.all():
        words = device.keywords.split(',')

        # Buscamos dispositivo
        for w in words:
            for t in text_split:
                if w in t:
                    devide_found = True

                    # Buscamos accion
                    for action in device.action_set.all():
                        action_keys = action.keywords.split(',')
                        for a in action_keys:
                            for t_a in text_split:
                                if a in t_a:
                                    # Formar la URL
                                    get_url = url_tarla.format(device=device.name, action=action.name)

                                    # Contestar
                                    # return HttpResponse(get_url)
                                    return HttpResponseRedirect(get_url)

    # Mostrar motivo de error
    if devide_found:
        Log.objects.create(type='ACTION_NOT_FOUND', text=text)
        return HttpResponse('Action not found.' + test)
    else:
        Log.objects.create(type='DEVICE_NOT_FOUND', text=text)
        return HttpResponse('Device not found.')
