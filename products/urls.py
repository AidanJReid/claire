from django.conf.urls import url, include
from .views import all_products, Detail

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'detail/<product.id>', Detail.as_view(), name="detail"),
]