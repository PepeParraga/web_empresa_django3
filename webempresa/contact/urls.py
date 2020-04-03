from django.urls import path
from . import views

urlpatterns = [
    ## Paths Contact
    path('', views.contact, name="contact"),
]
