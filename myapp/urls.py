from django.urls import path
from .views import listing, property_detail, add_property, tenant_management,add_unit,add_tenant

urlpatterns = [
    path('listing/', listing, name='property_listing'),
    path('property/<int:property_id>/', property_detail, name='property_detail'),
    path('tenant_management/', tenant_management, name='tenant_management'),
    path('addproperty/', add_property, name='add_property'),
    path('property/<int:property_id>/add_unit/', add_unit, name='add_unit'),
    path('unit/<int:unit_id>/add_tenant/', add_tenant, name='add_tenant'),
]