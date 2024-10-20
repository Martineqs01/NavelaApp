from django.urls import path
from .views import home, clients, exit, payments, citas
from . import views


urlpatterns = [
    path('', home, name='home'),
    path('clients/', clients, name='clients'),
    path('logout/', exit, name='exit'),
    path('registro/', views.register, name='register'),
    path('pagos/', payments, name='payments'),
    path('citas/', citas, name='citas'),

]
