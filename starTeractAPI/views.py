import json
import jwt
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import User, Talent
from .classes.UserClass import UserClass
from .classes.TalentClass import TalentClass
from .classes.CategoryClass import CategoryClass
from .classes.ClassificationClass import ClassificationClass
from django.views.decorators.csrf import csrf_exempt
import django.middleware
import requests


# Create your views here.

@csrf_exempt
def signUp(request):
    user = UserClass()
    if user.signUp(json.loads(request.body)):
        return JsonResponse({"success": True})
    return JsonResponse({"success": False})

@csrf_exempt
def signUpAsTalent(request):
    talent = TalentClass()
    if talent.signUp(json.loads(request.body)):
        return JsonResponse({"success": True})
    return JsonResponse({"success": False})


@csrf_exempt
def login(request):
    talent = TalentClass()
    return JsonResponse(talent.login(json.loads(request.body)))

@csrf_exempt
def getCategories(request):
    return JsonResponse(CategoryClass.getCategories(), safe=False)

@csrf_exempt
def test(request):
     return True

@csrf_exempt
def checkValidToken(request):
    try:
        decodedToken = jwt.decode(json.loads(request.body).get("token"), "django-insecure-olcf)=r)pwgqpnc3jcvob#abk*#k29mw!zp=2taufgvfm&)-v0", algorithms=["HS256"])
        return JsonResponse({"message": "token is valid"}, safe=False)
    except:
        return JsonResponse({"message": "invalid token"}, safe=False)

@csrf_exempt
def getTalents(request):
    return JsonResponse({
        "talents": TalentClass.getTalents(),
        "classifications": ClassificationClass.getSavedClassifications()
    })



@csrf_exempt
def getUserData(request):
    return JsonResponse(UserClass.getUserData(json.loads(request.body)))


@csrf_exempt
def getTalent(request):
    return  JsonResponse(TalentClass.getTalentByName(json.loads(request.body).get("name")))








