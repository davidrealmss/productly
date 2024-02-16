from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Producto, Categoría
from .forms import ProductoForm
# Create your views here.


def index(request):
    productos = list(Producto.objects.all())
    mensaje = 'Productos VOLEIBOL'
    data_response = [mensaje] + productos
    # return JsonResponse(data_response, safe=False)
    # return redirect("https://www.costasurestates.com")
    return render(
        request, 'index.html',
        context={'productos': productos}
    )


def detalle(request, product_id):
    try:
        producto = Producto.objects.get(id=product_id)
        return render(
            request, "detalle.html",
            context={'producto': producto})

    except Producto.DoesnotExist:
        raise Http404()


def formulario(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/productos')
    else:
        form = ProductoForm()
    return render(
        request,
        'producto_form.html',
        {'form': form}
    )

# hay una funcion que se encarga de hacer esto mismo evitando usar el try, except y evantar un Http404
# la funcion se llama get_object_or_404() viene con shortcuts,
    # get_object_or_404(Producto, id=product_id)
