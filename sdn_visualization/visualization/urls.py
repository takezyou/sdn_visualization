from django.urls import path
from . import views

urlpatterns = [
    path('show', views.show, name='show'),
    path('edit', views.edit, name='edit'),
    path('addvlan', views.addvlan, name='addvlan'),
    path('update', views.update, name='update'),
    path('vlans', views.vlans_index, name='vlans_index'),
    path('vlans_show/<int:vlanid>', views.vlans_show, name='vlans_show'),
    path('vlans_del', views.vlans_del, name='vlans_del'),
]