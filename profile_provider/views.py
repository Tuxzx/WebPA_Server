from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
import json

# Create your views here.
def index(request):
    return HttpResponse("Hello, world.")

def getPersonAll(request):
    all_entries = Person.objects.all()
    result = dict()
    for person in all_entries:
        temp = dict()
        temp['introduction']=person.introduction
        temp['background']=person.background
        temp['looks']=person.looks
        temp['character']=person.character
        temp['ability']=person.ability
        temp['weakness']=person.weakness
        temp['extend']=person.extend
        result[str(person.name)] = temp
    return HttpResponse(json.dumps(result, ensure_ascii=False), content_type='application/json; charset=utf-8')