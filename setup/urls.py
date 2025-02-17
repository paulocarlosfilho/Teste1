from django.contrib import admin
from django.urls import path
from to_do.views import to_do_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', to_do_list)
]
