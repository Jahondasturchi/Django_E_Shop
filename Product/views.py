from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models.category import  Categor
from .models.products import Product
from django.views.generic.edit import UpdateView, DeleteView,CreateView
from .forms import ProructForm, ProructFormNew
from django.urls import reverse_lazy
# Create your views here.
def ProductSavat(request):
    print(request.GET['inputname'])
    return render(request, 'savat.html')

class ProductCreate(CreateView):
    model = Product
    template_name = 'create.html'
    form_class = ProructFormNew
    success_url = reverse_lazy('base')

class ProductDelete(DeleteView):
    model = Product
    template_name = 'delete.html'
    success_url = reverse_lazy('base')

class ProductEdit(UpdateView):
    model = Product
    template_name = 'edit.html'
    form_class = ProructForm
    success_url = reverse_lazy('base')

class Base(ListView):
    model = Categor
    template_name = 'base.html'
    context_object_name = 'categors'


class ProductList(ListView):
    model = Product
    template_name = 'detail.html'
    context_object_name = 'productlist'
    
class ProductDetail(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product_detail'