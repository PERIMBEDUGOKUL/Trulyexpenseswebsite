from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('add-expenses',views.add_expenses, name='add-expenses'),
]