from django.http import HttpResponse
import datetime


def home(request):
    return HttpResponse("Welcome")


def today(request):
        dia = datetime.datetime.now()
        dia_try = f"Today is:  {dia}"
        return HttpResponse(dia_try)
