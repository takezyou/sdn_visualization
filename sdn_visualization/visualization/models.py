from django.db import models

class Topologies(models.Model):
    id = models.AutoField(primary_key=True)
    dport1 = models.CharField(max_length=200)
    dport2 = models.CharField(max_length=200)
    delay = models.FloatField(max_length=200)
    judge = models.CharField(max_length=200)
    updated = models.IntegerField()

class Vlans(models.Model):
    vlanid = models.IntegerField(primary_key=True)
    start = models.CharField(max_length=200)
    end = models.CharField(max_length=200)
    path = models.CharField(max_length=200)
    created_at = models.CharField(max_length=200)
    updated_at = models.CharField(max_length=200)

    def __str__(self):
        return self.vlanid