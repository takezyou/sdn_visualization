from django.contrib import admin


from .models import Topologies, Vlans

admin.site.register(Topologies)
admin.site.register(Vlans)
