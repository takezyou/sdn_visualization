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
    i = []
    j = []
    t = Topologies.objects.all()
    for topo in t:
        i.append([topo.dport1, topo.dport2, topo.delay, topo.judge])
    v = Vlans.objects.all()
    for vlan in v:
        j.append([vlan.vlanid, vlan.start, vlan.end, vlan.path])
    topologies = { 'topologies' : i , 'vlans' : j }

    return render(request, 'edit.html', topologies)

def addvlan(request):
    if request.method == 'GET':
        vlans = Vlans(vlanid=request.GET.get('newVlan'), start=request.GET.get('start'), end=request.GET.get('end'), path=request.GET.get('path'))
        vlans.save()
        return HttpResponse(status=200)
    

def update(request):
    if request.method == 'GET':
        path = request.GET.get('path')
        start = request.GET.get('start')
        end =  request.GET.get('end')
        if Vlans.objects.filter(start=start):
            v = Vlans.objects.get(start=start)
            v.path = path
            v.save()
            return HttpResponse(status=200)

        elif Vlans.objects.filter(end=start):
            v = Vlans.objects.get(end=start)
            v.path = path
            v.save()
            return HttpResponse(status=200)

def vlans_index(request):
    j = []
    v = Vlans.objects.all()
    vlans = { 'vlans' : v }

    return render(request, 'vlans_index.html', vlans)

def vlans_show(request, vlanid):
    i = []
    t = Topologies.objects.all()
    for topo in t:
        i.append([topo.dport1, topo.dport2, topo.delay, topo.judge])
    v = Vlans.objects.get(vlanid = vlanid)
    vi = v.path
    topologies = { 'topologies' : i , 'vlans' : vi }

    return render(request, 'vlans_show.html', topologies)

def vlans_del(request):
    if request.method == 'GET':
        v = Vlans.objects.get(vlanid = request.GET.get('vlan_id'))
        v.delete()

    return HttpResponse(status=200)


    