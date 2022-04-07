from http.client import HTTPResponse
from unittest import result
from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def lotto_basic(request):
    result = random.sample(range(1,46),6)
    return render(request, 'lotto_basic.html', {'lotto_result' : result})