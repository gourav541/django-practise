from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from .models import Feature

def index(request):
    feature1 = Feature()
    feature1.id=0
    feature1.name='FAST'
    feature1.details='This app is very FAST'

    feature2 = Feature()
    feature2.id=1
    feature2.name='RELIABLE'
    feature2.details='This app is very RELIABLE'

    feature3 = Feature()
    feature3.id=2
    feature3.name='PROBLEM SOLVING'
    feature3.details='This app is used for PROBLEM SOLVING'
    feature4 = Feature()
    feature4.id=3
    feature4.name='EASY TO ACCESS'
    feature4.details='This app is  EASY TO ACCESS'

    features = [feature1 ,feature2 ,feature3 , feature4]
    return render(request,'index.html',{'features': features})

def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request,'counter.html',{'amount': amount_of_words})


