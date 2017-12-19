from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Topologies,Vlans
 
def show(request):
    i = []
    t = Topologies.objects.all()
    for topo in t:
        i.append([topo.dport1, topo.dport2, topo.delay, topo.judge])
    topologies = { 'topologies' : i }
    return render(request, 'show.html', topologies)

def edit(request):
    return render(request, 'edit.html', )