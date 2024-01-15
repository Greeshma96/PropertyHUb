from django import forms
from .models import Property,Unit,Tenant

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'address', 'location']

class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['rent', 'unit_type']

class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ['name', 'address', 'document_proofs', 'unit', 'agreement_end_date', 'monthly_rent_date']
