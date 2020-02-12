from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Product


# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def detail(request, id):
    products = Products
    return render(request, "product-detail.html")


# class Detail(DetailView):
#     """
#     Detailed view of the treatment for
#     interested parties to understand more
#     and add to cart
#     """
#     model = Product
#     template_name = 'product-detail.html'
#     context_object_name = 'product'

#     def get_object(self, queryset=Product):
#         _id = self.kwargs.get('id')
#         instance = get_object_or_404(Product, id=_id)
#         return instance
    
#     def post(self, request, *args, **kwargs):
#         _id = self.kwargs.get('id')
#         instance = get_object_or_404(Product, id=_id)
#         product = self.get_object()
#         return redirect(request('product-detail.html', kwargs={product}))