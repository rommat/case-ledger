from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def clients_main(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<h1>КЛІЄНТИ</h1>')
