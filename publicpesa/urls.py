from django.contrib import admin
from django.urls import path
from counties import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('county/<int:county_id>/', views.county_detail, name='county_detail'),
]