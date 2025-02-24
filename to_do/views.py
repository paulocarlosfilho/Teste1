from datetime import date

from .models import To_do
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

import logging

logger = logging.getLogger(__name__)

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
        logger.info(f"Entrou na view to_do_complete com pk={pk}") # Log
        to_do = get_object_or_404(To_do, pk=pk)
        if to_do:
            logger.info(f"Objeto To_do encontrado: {to_do}") # Log
        else:
            logger.error("Objeto To_do não encontrado!")
        to_do.finished_at = date.today()
        to_do.save()
        logger.info(f"finished_at atualizado para {to_do.finished_at}") # Log
        return redirect("to_do_list")

