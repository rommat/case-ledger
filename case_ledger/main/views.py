from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def main(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<h1>ГОЛОВНА СТОРІНКА</h1>')
