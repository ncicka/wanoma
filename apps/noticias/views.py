from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required

from .models import Noticia, Categoria, Comentario

from django.urls import reverse_lazy

from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic import ListView
from .forms import NoticiaForm, FiltrarNoticiaForm, CategoriaForm

#@login_required
def Listar_Noticias(request):
	contexto = {}
	lista_categoria = []
	
	if request.GET: ## si hay valores que se mantengan los seleccionados
		form = FiltrarNoticiaForm(request.GET)
	else:
		form = FiltrarNoticiaForm()

	id_categoria = request.GET.get('id',None)
	fecha_desde = request.GET.get('fecha_desde',None)
	fecha_hasta = request.GET.get('fecha_hasta',None)
	ord_fecha = request.GET.get('orden_antiguedad',None)
	ord_alfab = request.GET.get('orden_alfabetico',None)

	if id_categoria:
		n = Noticia.objects.filter(categoria_noticia = id_categoria)
	else:
		n = Noticia.objects.all() #RETORNA UNA LISTA DE OBJETOS
 	
	# Filtrar solo si hay datos seleccionados en las fechas y
	# fecha_hasta es mayor o igual a fecha_desde
	if fecha_desde and fecha_hasta:
		if fecha_hasta >= fecha_desde:
			n = n.filter(fecha__range=[fecha_desde,fecha_hasta])

	ordenf='-'
	ordena=''
 
	if ord_fecha:
		ordenf = '' if ord_fecha == 1 else '-'

	if ord_alfab:
		ordena = '' if ord_alfab == 1 else '-'
	
	## si selecciona los dos tipos de orden los ordena primero fecha y luego por titulo
	if ord_fecha and ord_alfab:
		n = n.order_by(ordenf+'fecha',ordena+'titulo')
	elif ord_fecha: ## Si solo es orden por fecha
		n = n.order_by(ordenf+'fecha')
	elif ord_alfab: ## Si solo es orden alfabetico
		n = n.order_by(ordena+'titulo')
	else:
		n = n.order_by(ordenf+'fecha')
 
	cat = Categoria.objects.all().order_by('nombre')

	# Para el filtro por categorias
	lista_categoria.append(('','Todas las categorias'))
	
	for x in cat:
		lista_categoria.append((x.pk,x.nombre))			
     
	form.fields['id'].choices=lista_categoria
	
	contexto['noticias'] = n
	contexto['filtro_form']=form 

	return render(request, 'noticias/listar.html', contexto)

@login_required
def Detalle_Noticias(request, pk):
	contexto = {}

	n = Noticia.objects.get(pk = pk) #RETORNA SOLO UN OBEJTO
	contexto['noticia'] = n

	c = Comentario.objects.filter(noticia = n)
	contexto['comentarios'] = c

	return render(request, 'noticias/detalle.html',contexto)


@login_required
def Comentar_Noticia(request):

	com = request.POST.get('comentario',None)
	usu = request.user
	noti = request.POST.get('id_noticia', None)# OBTENGO LA PK
	noticia = Noticia.objects.get(pk = noti) #BUSCO LA NOTICIA CON ESA PK
	coment = Comentario.objects.create(usuario = usu, noticia = noticia, texto = com)

	return redirect(reverse_lazy('noticias:detalle', kwargs={'pk': noti}))

class Agregar_Noticia(CreateView):
	model=Noticia
	form_class = NoticiaForm
	success_url= reverse_lazy('noticias:listar')
	template_name= 'noticias/editar_agregar.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['titulo']='AGREGAR NOTICIA'
		return context
	
	def form_valid(self, form):
		noticia = form.save(commit=False)
		noticia.autor = self.request.user
		noticia.save()
		return super().form_valid(form)

class Editar_Noticia(UpdateView):
	model=Noticia
	form_class = NoticiaForm
	success_url= reverse_lazy('noticias:listar')
	template_name= 'noticias/editar_agregar.html'
 
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['titulo']='EDITAR NOTICIA'
		return context

class Borrar_Noticia(DeleteView):
	model = Noticia
	template_name='noticias/confirmar_borrar.html'
	success_url = reverse_lazy('noticias:listar')
 ## Vistas de Categorias
 
class Listar_Categoria(ListView):
	model=Categoria
	form_class = CategoriaForm
	context_object_name = 'categorias'
	success_url= reverse_lazy('noticias:listarcategoria')
	template_name= 'noticias/listar_categoria.html'
 
	def get_queryset(self):
		cat = Categoria.objects.order_by('nombre')
		return cat


class Agregar_Categoria(CreateView):
	model=Categoria
	form_class = CategoriaForm
	success_url= reverse_lazy('noticias:categoria')
	template_name= 'noticias/editar_agregar_categoria.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['titulo']='AGREGAR LA CATEGORIA'
		return context

class Editar_Categoria(UpdateView):
	model=Categoria
	form_class = CategoriaForm
	success_url= reverse_lazy('noticias:categoria')
	template_name= 'noticias/editar_agregar_categoria.html'
 
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['titulo']='EDITAR LA CATEGORIA'
		return context

class Borrar_Categoria(DeleteView):
	model = Categoria
	template_name='noticias/categoria_confirmar_borrar.html'
	success_url = reverse_lazy('noticias:categoria')

# Vistas de Comentario
class Borrar_Comentario(DeleteView):
	model = Comentario
	template_name='noticias/comentario_confirmar_borrar.html'

	def post(self, request, pk, noticia_pk):
		comentario = get_object_or_404(Comentario, pk=pk, noticia_id=noticia_pk)
		comentario.delete()
		return redirect('noticias:detalle', pk=noticia_pk)
 
#{'nombre':'name', 'apellido':'last name', 'edad':23}
#EN EL TEMPLATE SE RECIBE UNA VARIABLE SEPARADA POR CADA CLAVE VALOR
# nombre
# apellido
# edad

'''
ORM

CLASE.objects.get(pk = ____)
CLASE.objects.filter(campos = ____)
CLASE.objects.all() ---> SELECT * FROM CLASE

'''