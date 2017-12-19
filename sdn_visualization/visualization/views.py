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
        a = request.GET.get('newVlan')
        b = request.GET.ge('start')
        c = request.GET.get('end')
        d = request.GET.get('path')
        print(a, b, c, d)
        vlans = Vlans(vlanid=request.GET['newVlan'], start=request.GET['start'], end=request.GET['end'], path=request.GET['path'])
        vlans.save()

def update(request):
    v = Vlans.objcts.all()
    start = request.GET['start']
    end =  request.GET['end']
    print(start, end)
    # if Vlan.find_by(start: params[:start]):
    #     Vlan.find_by(start: params[:start]).update_attributes(start: params[:start], end: params[:end], path: params[:path])
    # elif Vlan.find_by(end: params[:start]):
    #     Vlan.find_by(end: params[:start]).update_attributes(start: params[:start], end: params[:end], path: params[:path])
