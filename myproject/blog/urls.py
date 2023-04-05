from django.urls import path
from blog import views

urlpatterns = [
    # path('', views.Index),
    path('', views.welcome),
    path('new', views.new)
]