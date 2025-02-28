from datetime import date

from .models import To_do, ArquivoDownload
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render



def to_do_list(request):
    to_do = To_do.objects.all()
    return render(request, 'to_do/to_do_list.html', {"to_do_list": to_do_list})

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

class to_do_complete_view(View):
    def get(self, request, pk):
        to_do = get_object_or_404(To_do, pk=pk)
        to_do.finished_at = date.today()
        to_do.save()
        
        return redirect("to_do_list")

class downloads_view(View):
    def get(self, request):
        arquivo = ArquivoDownload.objects.all()
        return render(request, 'download_table.html', {'arquivos': arquivo})      
