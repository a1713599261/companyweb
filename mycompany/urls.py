from django.urls import path
from django.contrib import admin
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('product/<int:idx>/', views.product, name='product'),
    path('about/<int:idx>/', views.about, name='about'),
    # path(r'^about/(?P<idx>\d+)/(?P<cate_id>\d+)$', views.about, name='about'),
    path('job/<int:idx>/', views.job, name='job'),
    path('contact/<int:idx>/', views.contact, name='contact'),
]