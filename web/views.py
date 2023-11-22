from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import CalculadoraForm

# Create your views here.

def calcular(request):
    cant_max = 313
    result = None
    message = None

    if request.method == 'POST':
        form = CalculadoraForm(request.POST)
        if form.is_valid():
            number1 = form.cleaned_data['number1']
            number2 = form.cleaned_data['number2']
            number3 = form.cleaned_data['number3']
            number4 = form.cleaned_data['number4']
            number5 = form.cleaned_data['number5']
            number6 = form.cleaned_data['number6']
            number7 = form.cleaned_data['number7']
            number8 = form.cleaned_data['number8']
            number9 = form.cleaned_data['number9']
            operation = form.cleaned_data['operation']
           
            if operation == '+':
                result = number1 + number2 + number3 + number4 + number5 + number6 + number7 + number8 + number9 
 
                if result > cant_max:
                    message= f", Estas desperdiciando agua, Revisa nuestra pagina para ver recomendaciones de como ahorrar agua"
                elif result < cant_max:
                    message= f", Estas ahorrando agua, bien hecho"
                else:
                    message = f", estás utilizando la cantidad justa de agua. ¡Excelente!"
            

            elif operation == '%':
                result = (number1 + number2 + number3 + number4 + number5 + number6 + number7 + number8 + number9)/100 
                if result > cant_max:
                    message = f", Estas desperdiciando agua, Revisa nuestra pagina para ver recomendaciones de como ahorrar agua"
                elif result < cant_max:
                    message= f", Estas ahorrando agua, bien hecho"
                else:
                    message = f", estás utilizando la cantidad justa de agua. ¡Excelente!"

    else:
        form = CalculadoraForm()
        
    
    return render(request, 'index.html', {'form': form, 'result': result, 'message': message})