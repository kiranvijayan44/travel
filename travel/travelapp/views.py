from django.shortcuts import render
from .models import Place, Team


def demo(request):
    obj = Place.objects.all()
    obj2 = Team.objects.all()
    return render(request, "index.html", {'result': obj, 'result1': obj2},)
