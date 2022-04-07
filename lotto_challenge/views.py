from http.client import HTTPResponse
from unittest import result
from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def lotto_challenge(request):
    return render(request, 'lotto_challenge.html')

def lotto_result(request):
    gamecount = request.GET.get('gamecount')
    result = []

    if int(gamecount) > 0 :
        for i in range(1, int(gamecount)+1):
            result.append(random.sample(range(1,46),6))
    else :
        result = ['Error']

    return render(request, 'lotto_result.html', {'lotto_result' : result, 'gamecount' : gamecount})
