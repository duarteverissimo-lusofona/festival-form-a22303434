from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('dias/', views.dias_view, name='dias'),
    path('palcos/', views.palcos_view, name='palcos'),
    path('concertos/<int:concerto_id>/', views.concerto_view, name='concerto'),
    path('concertos/<int:concerto_id>/editar/', views.editar_concerto_view, name='editar_concerto'),
]
