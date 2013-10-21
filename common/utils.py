# -*- coding: utf-8 -*-

import os
import random
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson


def direct_response(request, *args, **kwargs):
    """
    Forma resumida de render_to_response, enviando context_instance al template
    """
    kwargs['context_instance'] = RequestContext(request)
    return render_to_response(*args, **kwargs)


def json_response(data):
    """
    Devuelve una respuesta json con la información de data
    """
    return HttpResponse(simplejson.dumps(data), mimetype='application/json')


def highlyRandomName(filename, longitud=20):
    """
    retorna un nombre aleatorio de longitud igual a 'longitud',
    manteniendo la extension de la imagen
    """
    lista_letras_numeros = \
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    name = \
        "".join([random.choice(lista_letras_numeros) for i in xrange(longitud)])
    root, ext = os.path.splitext(filename)

    return name + ext
