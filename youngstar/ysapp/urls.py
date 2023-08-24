from django.urls import path
from . import views
app_name = 'ysapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('person/<int:person_id>/', views.detail, name='detail'),
    path('add/', views.add_person, name='add_person'),



]
