from django.shortcuts import render
from .forms import ContactoForm

def contacto(request):
    data = {'form': ContactoForm(), 'mensaje': ""}
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            data["mensaje"] = "Contacto guardado"
            formulario.save()
        else:
            data["form"] = formulario
    return render(request, 'contacto.html', data)

def contacto_whats(request):
    return render(request, 'contacto_wha.html', {})