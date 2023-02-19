from django.urls import path,include
from .views import *
urlpatterns = [
    path('', home, name="home"),
    path('<int:id>/about', about, name="about"),
    path('deals/', deal, name="deals"),
    path('<int:id>/reservation/', reservation, name="reservation"),
]