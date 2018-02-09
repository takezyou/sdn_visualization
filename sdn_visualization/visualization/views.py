from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Topologies,Vlans,Hosts
import re
 
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
        path = request.GET.get('path')
        path_length = re.split('[|,]',path)
        path_length.remove(path_length[0])
        path_length.remove(path_length[-1])
        vlans = Vlans(vlanid=request.GET.get('newVlan'), start=request.GET.get('start'), end=request.GET.get('end'), path=request.GET.get('path'), path_length=len(path_length))
        vlans.save()
        return HttpResponse(status=200)
    

def update(request):
    if request.method == 'GET':
        path = request.GET.get('path')
        start = request.GET.get('start')
        end =  request.GET.get('end')
        path_length = re.split('[|,]',path)
        path_length.remove(path_length[0])
        path_length.remove(path_length[-1])
        if Vlans.objects.filter(start=start):
            v = Vlans.objects.get(start=start)
            v.path = path
            v.path_length = len(path_length)
            v.save()
            return HttpResponse(status=200)

        elif Vlans.objects.filter(end=start):
            v = Vlans.objects.get(end=start)
            v.path = path
            v.path_length = len(path_length)
            v.save()
            return HttpResponse(status=200)

def vlans_index(request):
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

def vlans_del(request, vlanid):
    v = Vlans.objects.get(vlanid = vlanid)
    v.delete()
    id = {'vlan_id' : vlanid}

    return render(request, 'vlans_delete.html', id)

def vlans_control(request, vlanid):
    v = Vlans.objects.get(vlanid = vlanid)
    start = v.start
    end = v.end
    path = v.path
    path = re.split('[|,]',path)
    if 4 < len(path):
        del path[0:2]
        del path[-2]
        del path[-1]
    else:
        path = []
    path_port = v.path
    path_port = re.split('[|,]',path_port)
    path_port1 = path_port[1].split("-")
    path_port2 = path_port[-2].split("-")
    in_port1_2 = path_port1[1]
    in_port2_2 = path_port2[1]
    t1 = Topologies.objects.get(dport1=start)
    t2 = Topologies.objects.get(dport1=end)
    port_name1 = t1.dport2
    port1 = t1.dport1
    port_1 = port1.split("-")
    in_port1_1 = port_1[1]
    port_name2 = t2.dport2
    port2 = t2.dport1
    port_2 = port2.split("-")
    in_port2_1 = port_2[1]
    ip1 = Hosts.objects.get(host_name=port_name1)
    ip2 = Hosts.objects.get(host_name=port_name2)
    ip_address1 = ip1.ip_address
    ip_address2 = ip2.ip_address
    datapath1 = start.split("-")
    datapath2 = end.split("-")
    if int(datapath1[0]) < 10:
        datapath1 = "000000000000000" + datapath1[0]
    else:
        datapath1 = "00000000000000" + datapath1[0]
    
    if int(datapath2[0]) < 10:
         datapath2 = "000000000000000" + datapath2[0]
    else:
         datapath2 = "00000000000000" + datapath2[0]

    vlans = { 'vlans': vlanid, 'path': path, 'port_name1':port_name1, 'port_name2':port_name2, 'datapath1': datapath1, 'datapath2':datapath2, 'ip_address1':ip_address1, 'ip_address2':ip_address2, 'in_port1_1':in_port1_1, 'in_port2_1':in_port2_1, 'in_port1_2':in_port1_2, 'in_port2_2':in_port2_2}

    return render(request, 'vlans_control.html', vlans)

def ipaddress(request):
    h = Hosts.objects.order_by("host_name")
    host = { 'host':h }

    return render(request, 'ipaddress.html', host)

def addip(request):
    if request.method == 'GET':
        host = request.GET.get('host_name')
        ip = request.GET.get('ip_address')
        h = Hosts(host_name=host, ip_address=ip)
        h.save()
        return HttpResponse(status=200)

def delip(request):
    if request.method == 'GET':
        host = request.GET.get('host_name')
        h = Hosts.objects.get(host_name=host)
        h.delete()

        return HttpResponse(status=200)