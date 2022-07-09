from . import views
from django.urls import path

urlpatterns = [
    path('form', views.form, name='form'),
    path('postform', views.postForm, name='postform'),
    path('detail/<str:id>', views.detail, name='detail'),
    path('absen/<str:id>', views.absen, name='absen'),
]