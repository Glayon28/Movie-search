from django.http import HttpResponse,HttpResponseNotFound,Http404
from django.shortcuts import render, redirect


def index(request): #HttpRequest
    return HttpResponse("сторінка програми Movier.")

def categories(request, filmid):
    if(request.GET):
       print(request.GET)
    return HttpResponse(f"<h1> Статті за категоріями</h1><p>{filmid}</p>")

def archive(request, year):
    if int(year) >2022:
        return redirect('home', permanent=False)


    return HttpResponse(f"<h1>Архів по рокам</h1><p>{year}</p>")

def pageNotFound(request, exeption):
    return HttpResponseNotFound('<h1>Архів по рокам</h1>')