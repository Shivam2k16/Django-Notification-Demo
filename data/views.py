from datetime import date
from django.shortcuts import render, redirect

# Create your views here.
from data.forms import AddTruckForm,NotificationForm
from data.models import AddTruck, Notification


def addtruck(request):
    if request.method == 'POST':
        form = AddTruckForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request,'data/new_truck.html',{'form':form})
    else:
        form = AddTruckForm()
    return render(request,'data/new_truck.html',{'form':form})


def notification(request):
    lists=AddTruck.objects.all()
    current_date=date.today()
    for i in lists:
        insurance_left=''
        remaining = i.insurance_date - current_date
        remaining = str(remaining)
        for j in remaining:
            if j == ' ':
                break
            insurance_left += j
        fitness_left = ''
        remaining = i.fitness_date - current_date
        remaining = str(remaining)
        for j in remaining:
            if j == ' ':
                break
            fitness_left += j
        pollution_left = ''
        remaining = i.pollution_date - current_date
        remaining = str(remaining)
        for j in remaining:
            if j == ' ':
                break
            pollution_left += j

        truck_available = Notification.objects.filter(truck_number=i.truck_number)
        if truck_available:
            truck_available.update(remaining_insurance = insurance_left,remaining_fitness= fitness_left,remaining_pollution=pollution_left)
        else:
            Notification.objects.create(truck_number = i.truck_number,insurance_date=i.insurance_date,fitness_date= i.fitness_date,pollution_date=i.pollution_date,
                                        remaining_insurance=insurance_left, remaining_fitness=fitness_left,
                                        remaining_pollution=pollution_left,remainder= 0,read = 0,
                                        remainded_day_insurane=31,remainded_day_fitness=31,remainded_day_pollution=31)
    notify = Notification.objects.all()
    for i in notify:
        if i.remaining_insurance <=30 or i.remaining_fitness <=30 or i.remaining_pollution <=30:
            i.remainder = True
            i.save()
        if i.remaining_insurance <= 7 :
            if i.remainded_day_insurane !=7:
                i.remainded_day_insurane = 7
                i.read=False
                i.save()
        elif i.remaining_insurance <= 15:
            if i.remainded_day_insurane != 15:
                i.remainded_day_insurane = 15
                i.read = False
                i.save()
        elif i.remaining_insurance <= 30:
            if i.remainded_day_insurane != 30:
                i.remainded_day_insurane = 30
                i.read = False
                i.save()

        if i.remaining_fitness <= 7 :
            if i.remainded_day_fitness !=7:
                i.remainded_day_fitness = 7
                i.read=False
                i.save()
        elif i.remaining_fitness <= 15:
            if i.remainded_day_fitness != 15:
                i.remainded_day_fitness = 15
                i.read = False
                i.save()
        elif i.remaining_fitness <= 30:
            if i.remainded_day_fitness != 30:
                i.remainded_day_fitness = 30
                i.read = False
                i.save()
        if i.remaining_pollution <= 7 :
            if i.remainded_day_pollution !=7:
                i.remainded_day_pollution = 7
                i.read=False
                i.save()
        elif i.remaining_pollution <= 15:
            if i.remainded_day_pollution != 15:
                i.remainded_day_pollution = 15
                i.read = False
                i.save()
        elif i.remaining_pollution <= 30:
            if i.remainded_day_pollution != 30:
                i.remainded_day_pollution = 30
                i.read = False
                i.save()
    filtered_notify = Notification.objects.filter(remainder=True,read=False)
    seven=7
    fifteen = 15
    thirty = 30
    return render(request,'data/notification.html',{'notify':filtered_notify,'seven':seven,'fifteen':fifteen,'thirty':thirty})


def notification_mark(request,pk):
    list = Notification.objects.filter(truck_number=pk)
    for i in list:
        i.read = True;
        i.save()
    return redirect('notification')