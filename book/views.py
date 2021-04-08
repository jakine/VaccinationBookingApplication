from django.shortcuts import render, redirect
from .forms import ReservationForm
# Create your views here.

def index(request):
    context = {}
    reservation_form = ReservationForm()
    context['reservation_form'] = reservation_form


    if request.method == 'POST':
        reservation_form = ReservationForm(request.POST)
        if reservation_form.is_valid():
            return redirect(reservation_message)

    return render(request, 'index.html', context)




def reservation_message(request):
    context = {}
    return render(request, 'reservation_message.html', context)