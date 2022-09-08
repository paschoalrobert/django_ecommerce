from django import forms

class ContactForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Nome completo"
                }
            )
        )
    email     = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Email"
                }
            )
        )
    content   = forms.CharField(
        widget=forms.Textarea(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Mensagem"
                }
            )
        )
