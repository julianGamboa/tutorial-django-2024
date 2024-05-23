from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):
  return HttpResponse("(INDEX), world. You're at the polls index.")


def dia_5(request):
  return HttpResponse("http://localhost:8000/front/dia 5")


def dia_1(request):

  return render(request, 'libro/actualizar_libro_alonzo.html')
