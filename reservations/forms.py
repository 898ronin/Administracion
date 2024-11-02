from django import forms
from .models import Client, Reservation, Department
from django.core.exceptions import ValidationError

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['nombre', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['cliente', 'propiedad', 'fecha_inicio', 'fecha_fin']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("fecha_inicio")
        end_date = cleaned_data.get("fecha_fin")

        if start_date and end_date:
            if start_date > end_date:
                raise ValidationError("La fecha de inicio debe ser anterior a la fecha de fin.")
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cliente'].queryset = Client.objects.all()
        self.fields['propiedad'].queryset = Department.objects.filter(disponibilidad=True)


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['nombre', 'descripcion', 'capacidad', 'disponibilidad']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'capacidad': forms.NumberInput(attrs={'class': 'form-control'}),
        }
