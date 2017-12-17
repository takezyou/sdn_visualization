from django.shortcuts import render
from django.http.response import HttpResponse
 
def show(request):
    return render(request, 'show.html')