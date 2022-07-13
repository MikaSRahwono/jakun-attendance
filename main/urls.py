from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('form', views.form, name='form'),
    path('postform', views.postForm, name='postform'),
    path('detail/<str:id>', views.detail, name='detail'),
    path('absen/<str:id>', views.absen, name='absen'),
    path('search', views.search, name='search'),
    path('postsearch', views.postsearch, name='postsearch'),
    path('faq', views.faq, name='faq')

]