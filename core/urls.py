from django.urls import path

from core.views import contato, index

urlpatterns = [
    path('', index),
    path('contato/', contato)
]