from django import forms

from data.models import AddTruck ,Notification


class AddTruckForm(forms.ModelForm):
    class Meta:
        model = AddTruck
        exclude = []

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        exclude=[]