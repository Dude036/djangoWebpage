from django.shortcuts import render
from django.template import context
from django.db.models import F
from home.models import currentTime
from time import gmtime, strftime
import datetime

# Home page response
def index(request):
    time = strftime("%H:%M:%S", gmtime())
    date = strftime("%m-%d-%Y", gmtime())
    strftime("%Y-%m-%d %H:%M:%S", gmtime())
    return render(request, 'index.html', context = {'date':date , 'time':time})
