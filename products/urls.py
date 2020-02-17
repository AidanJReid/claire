from django.conf.urls import url, include
from .views import all_products, detail

urlpatterns = [
    url(r'', all_products, name='products'),
    url(r'products/^(?P<id>\d+)', detail, name='detail')
]