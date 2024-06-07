from django.urls import path
from inicio import views


urlpatterns = [
    path('', views.inicio),
    path('template1/', views.template1),
    path('template4/<str:nombre>/<str:apellido>/<int:edad>', views.template4),
    path('probando/', views.probando, name="probando"),
    path('autos/crear/<str:marca>/<str:modelo>', views.crear_auto)
    # path('autos/crear/<str:marca>/<str:modelo>', views.crear_auto_v2, name="crear auto")
    
]
