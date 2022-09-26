from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('body/<int:pk>', views.contents, name='body')
]