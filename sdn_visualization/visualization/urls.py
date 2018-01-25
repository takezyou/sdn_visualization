from django.urls import path
from . import views

urlpatterns = [
    path('show', views.show, name='show'),
    path('edit', views.edit, name='edit'),
    path('addvlan', views.addvlan, name='addvlan'),
    path('update', views.update, name='update'),
    path('ipaddress', views.ipaddress, name='ipaddress'),
    path('addip', views.addip, name='addip'),
    path('delip', views.delip, name='delip'),
    path('vlans', views.vlans_index, name='vlans_index'),
    path('vlans_show/<int:vlanid>', views.vlans_show, name='vlans_show'),
    path('vlans_del/<int:vlanid>', views.vlans_del, name='vlans_del'),
    path('vlans_control/<int:vlanid>', views.vlans_control, name='vlans_control'),
]