from django import forms

class CalculadoraForm(forms.Form):
    number1 = forms.FloatField(label='Baño')
    number2 = forms.FloatField(label='Lavado de mano ')
    number3 = forms.FloatField(label='Lavado de ropa')
    number4 = forms.FloatField(label='Cocina')
    number5 = forms.FloatField(label='Lavado de auto')
    number6 = forms.FloatField(label='Ducha') 
    number7 = forms.FloatField(label='Limpieza de hogar')
    number8 = forms.FloatField(label='Riego de jardin')
    number9 = forms.FloatField(label='Agua personal')

    operation = forms.ChoiceField(choices=[('+', 'Sumar'), ('%', 'Porcentaje')])
