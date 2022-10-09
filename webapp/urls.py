from django.urls import path
from webapp import views


app_name = 'webapp'

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about')
]
