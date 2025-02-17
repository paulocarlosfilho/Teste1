from django.shortcuts import render
from .models import To_do

def to_do_list(request):
    to_do = To_do.objects.all()
    return render(request, 'to_do/to_do_list.html', {"to_dos": to_do})