
from django import forms
from datetime import date
from django import forms




class BookingForm(forms.Form):
    title = forms.CharField(label='Столик', widget=forms.TextInput(attrs={"class": "form-control"  }))
    content = forms.CharField(label='Имя клиента',widget=forms.TextInput(attrs={"class": "form-control"}))
    is_published = forms.BooleanField(label='Бронь подтверждена', required=False, initial=True)
    updated_at = forms.DateTimeField(label='Дата', widget=forms.TimeInput(attrs={"class": "form-control", 'type':'datetime-local' ,'value':"2020-11-11 13:45:00"}))