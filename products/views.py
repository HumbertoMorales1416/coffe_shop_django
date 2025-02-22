from django.urls import reverse_lazy
from django.views import generic
from products.forms import ProductForm
from products.models import Product

class ProductFormView(generic.FormView):
  template_name = 'products/add_product.html'
  form_class = ProductForm
  success_url = reverse_lazy('add_product')

  def form_valid(self, form):
    form.save()
    return super().form_invalid(form)
  
class ProductListView(generic.ListView):
  model: Product
  template_name = 'products/list_products.html'
  context_object_name = 'products'
  
  def get_queryset(self):
    return Product.objects.order_by('id')