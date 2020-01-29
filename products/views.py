from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import Product
from django.views.generic import DetailView

# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

class Detail(DetailView):
    """
    Detailed view of the treatment for
    interested parties to understand more
    and add to cart
    """
    model = Product
    template_name = "product-detail.html"
    context_object_name = 'product'
    extra_context = {}

    def get_object(self, queryset=Product):
        _id = self.kwargs.get('pk')
        instance = get_object_or_404(Product, id=_id)

        self.extra_context['product'] = instance
        return instance

    def post(self, request):
        _id = self.get('product.name')
        instance = get_object_or_404(Product, id=_id)
        product = self.get_object()
        return render(request("product-detail.html", {{product.id}}))