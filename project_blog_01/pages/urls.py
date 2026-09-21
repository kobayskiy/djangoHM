from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('pages/about', views.about, name='about'),
    path('pages/rule', views.rules, name='rules')
]
