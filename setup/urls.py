from django.contrib import admin
from django.urls import path
from to_do.views import To_do_List_View, To_Do_Created_View, to_do_update_view, to_do_delete_view, to_do_complete_view, downloads_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', To_do_List_View.as_view(), name="to_do_list"),
    path('creation', To_Do_Created_View.as_view(), name="to_do_creation"),
    path('update/<int:pk>', to_do_update_view.as_view(), name="to_do_update"),
    path('delete/<int:pk>', to_do_delete_view.as_view(), name="to_do_delete"),
    path('complete/<int:pk>', to_do_complete_view.as_view(), name='to_do_complete'),
    path('download', downloads_view.as_view(), name='download'),

]
