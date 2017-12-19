from django.urls import path
from . import views

urlpatterns = [
    path('show', views.show, name='show'),
    path('edit', views.edit, name='edit'),
    path('addvlan', views.edit, name='edit'),
    path('update', views.update, name='update'),
]