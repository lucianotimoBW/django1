from django.contrib import admin
from django.urls import path
from inicio.views import inicio, template1, template4, probando


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('template1/', template1),
    path('template4/<str:nombre>/<str:apellido>/<int:edad>', template4),
    path('probando_if_for/', probando),
]

