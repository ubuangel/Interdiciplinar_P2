from django.shortcuts import render
from .models import provedor, pedido, producto, Cliente
# Create your views here.
def home(request):
    
    return render(request,'appblog/home.html')
def servicios(request):
    
    return render(request,'appblog/servicios.html')

def tienda(request):
    
    return render(request,'appblog/tienda.html')

def blog(request):
    
    return render(request,'appblog/blog.html')

def contacto(request):
    
    return render(request,'appblog/contacto.html')

def calculo(request):
   # num_b=pedido.objects.all().count()
    num_Pr=provedor.objects.all().count()
    # Libros disponibles (status = 'a')
  #$  num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_p=producto.objects.count()  # El 'all()' esta implícito por defecto.
    
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'appblog/calculo.html',
        context={'num_Pr':num_Pr,'num_p':num_p},
    )
    