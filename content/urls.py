from django.urls import path
import content
from .views import ContactView
from . import views


urlpatterns = [
    path("",views.Home,name="index"),
    path("contact/",views.ContactView,name="contact"),
]
