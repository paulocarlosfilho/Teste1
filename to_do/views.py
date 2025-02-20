from .models import To_do
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def to_do_list(request):
    to_do = To_do.objects.all()
    return render(request, 'to_do/to_do_list.html', {"to_dos": to_do})

class To_do_List_View(ListView):
    model = To_do


class To_Do_Created_View(CreateView):
    model = To_do
    fields = ["title", "deadline"]
    success_url = reverse_lazy("to_do_list")

class to_do_update_view(UpdateView):
    model = To_do
    fields = ["title", "deadline"]
    success_url = reverse_lazy("to_do_list")

class to_do_delete_view(DeleteView):
    model = To_do
    fields = ["title", "deadline"]
    success_url = reverse_lazy("to_do_list")