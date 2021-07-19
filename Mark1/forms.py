from django import forms

from Mark1.models import login


class TraineeForm(forms.ModelForm):

    class Meta:
        model =login
        fields ='__all__'
        widgets = {
            "userid":forms.TextInput(
                attrs={
                    "placeholder": "First name",
                    "class": "txt"
                }
            ),
            "lastname": forms.TextInput(
                attrs={
                    "placeholder": "Enter Last name",
                    "class": "txts"
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Enter Email",
                    "class": "email"
                }
            ),
            "Password": forms.TextInput(
                attrs={
                    "placeholder": "Enter Password",
                    "class": "psw"
                }
            ),
            "phone": forms.NumberInput(
                attrs={
                    "placeholder": "Enter Phone number",
                    "class": "num"
                }
            ),

        }

