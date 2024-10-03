# from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookingForm, TrackBookingForm
from .models import Menu, Booking
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def home(request):
    print('rendering home...')
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        data = BookingForm(request.POST)
        if data.is_valid():
            saved = data.save()
            ctx = {'first_name': saved.first_name, 'last_name': saved.last_name, 'reference': saved.reference, 'guests': saved.guest_number, 'note': saved.comment}
            return render(request, 'booking_successful.html', ctx)
    context = {'form':form}
    return render(request, 'book.html', context)


def track(request):
    form = TrackBookingForm()

    if request.method == 'POST':
        form = TrackBookingForm(request.POST)
        if form.is_valid():  # Validate the form first
            reference = form.cleaned_data['reference']
            
            try:
                booking = Booking.objects.get(reference=reference)
                ctx = {
                    'first_name': booking.first_name,
                    'last_name': booking.last_name,
                    'reference': booking.reference,
                    'guests': booking.guest_number,
                    'note': booking.comment,
                }
                return render(request, 'booking_successful.html', ctx)
            
            except Booking.DoesNotExist:
                ctx = {'form': form, 'error': 'No booking found with that reference.'}
                return render(request, 'track.html', ctx)

    context = {'form': form}
    return render(request, 'track.html', context)


# Add your code here to create new views
def menu(request):
    menu_data = Menu.objects.all().order_by("name")
    maindata = {"menus": menu_data}
    template_name = "menu.html"
    return render(request, template_name, maindata) 

def display_menu_item(request, pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ""
    return render(request, "menu_item.html", {"menu_item": menu_item})