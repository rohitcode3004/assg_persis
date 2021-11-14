import django_filters
from django_filters import CharFilter
from .models import Router

class RouterFilter(django_filters.FilterSet):
	SapId = CharFilter(field_name='sapid', lookup_expr='icontains')
	Hostname = CharFilter(field_name='hostname', lookup_expr='icontains')
	Loopback = CharFilter(field_name='loopback', lookup_expr='icontains')
	MacAddress = CharFilter(field_name='mac_address', lookup_expr='icontains')

	class Meta:
		model = Router
		exclude = ['sapid', 'hostname', 'mac_address', 'loopback']