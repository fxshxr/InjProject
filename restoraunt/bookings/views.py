from django.shortcuts import render ,  redirect
from django.http import HttpResponse
from .forms  import BookingForm
from .models import Bookings

# Create your views here.

def index(request):
    booking = Bookings.objects.all()
    return render(request, 'bookings/index.html',{'bookings':booking,'title':'Список Бронирований'})


def add_bookings(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Bookings.objects.create(**form.cleaned_data)
            return redirect('home')

    else:
        form = BookingForm()

    return render(request,'bookings/add_bookings.html', {'form':form , 'title':'Список Бронирований'})
 
def applied(request):
    booking = Bookings.objects.all()
    return render(request,'bookings/applied.html', {'bookings':booking,'title':'Подтвержденные бронирования'})


