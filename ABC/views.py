from django.shortcuts import render

from data.models import AddTruck


def home(request):
    trucks = AddTruck.objects.all()
    return render(request,'data/home.html',{'trucks':trucks})