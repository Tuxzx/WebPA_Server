from django.shortcuts import render
from django.http import HttpResponse
from .models import Person, MessageBoard
import json
from django.utils import timezone

# Create your views here.
def index(request):
    return HttpResponse("Hello, world.")

def getPersonAll(request):
    all_entries = Person.objects.all()
    result = dict()
    for person in all_entries:
        temp = dict()
        temp['name'] = person.name
        temp['introduction']=person.introduction
        temp['background']=person.background
        temp['looks']=person.looks
        temp['character']=person.character
        temp['ability']=person.ability
        temp['weakness']=person.weakness
        temp['extend']=person.extend
        result[str(person.id)] = temp
    return HttpResponse(json.dumps(result, ensure_ascii=False), content_type='application/json; charset=utf-8')

def getMessageAll(request):
    all_entries = MessageBoard.objects.filter(titleid=int(request.GET['fperson_id']))
    result = dict()
    for msg in all_entries:
        temp = dict()
        temp['nickname'] = msg.nickname
        temp['message']=msg.message
        result[str(msg.id)] = temp
    return HttpResponse(json.dumps(result, ensure_ascii=False), content_type='application/json; charset=utf-8')

def messageBoard(request):
    fnickname = request.POST['fnickname']
    fperson_id = request.POST['fperson_id']
    fmessage = request.POST['fmessage']
    msgbrd = MessageBoard(nickname=fnickname, titleid=int(fperson_id), message=fmessage,time=timezone.now())
    msgbrd.save()
    return HttpResponse("已发送")