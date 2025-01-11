from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def clients(request: HttpRequest) -> HttpResponse:
    return render(request, 'client/clients.html')
