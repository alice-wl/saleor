from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

class Client(TenantMixin):
    name        = models.CharField(max_length=100)
    schema_name = models.CharField(max_length=100)

class Domain(DomainMixin):
    domain        = models.CharField(max_length=100)
