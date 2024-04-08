from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    return render(request, 'home.html', {'value': datetime.datetime.now()})