from django import forms
from .models import Appointment


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment

        fields = [
            "name",
            "age",
            "gender",
            "phone",
            "email",
            "consultation_type",
            "appointment_date",
            "appointment_time",
            "problem",
        ]

        widgets = {

            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Full Name"
            }),

            "age": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Age"
            }),

            "gender": forms.Select(attrs={
                "class": "form-select"
            }),

            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Mobile Number"
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Email Address"
            }),

            "consultation_type": forms.Select(attrs={
                "class": "form-select"
            }),

            "appointment_date": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),

            "appointment_time": forms.TimeInput(attrs={
                "class": "form-control",
                "type": "time"
            }),

            "problem": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5,
                "placeholder": "Describe your concern..."
            }),
        }