# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 19:50:26 2018

@author: LBS
"""

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")