import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from myanalysis import MyAnalysis


def home(request):
    return render(request, 'index.html')

def d1(request):
    context = {'section':'d1.html'}
    return render(request, 'index.html', context)

def dls(request):
    option = request.GET['option']
    data = MyAnalysis.Titanic().t1(option)
    return HttpResponse(json.dumps(data), content_type='application/json')

def d2(request):
    context = {'section': 'd2.html'}
    return render(request, 'index.html', context)

def d3(request):
    context = {'section': 'd3.html'}
    return render(request, 'index.html', context)

def d3s(request):
    startDt = request.GET['startDt']
    endDt = request.GET['endDt']
    data = MyAnalysis.Open().o1(startDt, endDt)
    return HttpResponse(json.dumps(data), content_type='application/json')

def d4(request):
    context = {'section': 'd4.html'}
    return render(request, 'index.html', context)

def d5(request):
    context = {'section': 'd5.html'}
    return render(request, 'index.html', context)

def geo(request):
    context = {'section': 'geo.html'}
    return render(request, 'index.html', context)