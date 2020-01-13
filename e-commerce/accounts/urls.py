from django.conf.urls import url, include
from . import urls_reset
from .views import index, register, profile, logout, login
from accounts.views import logout, login, registration, user_profile
from accounts import url_reset

urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', registration, name="registration"),
    url(r'^profile/', user_profile, name="profile"),
    url(r'^password-reset/', include(url_reset))
]