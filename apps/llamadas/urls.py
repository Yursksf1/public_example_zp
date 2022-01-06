from django.urls import path, include
from rest_framework import routers
from apps.llamadas import views

router = routers.DefaultRouter()
router.register(r'puntos', views.PuntoView, 'punto')
router.register(r'protocolo_llamadas', views.PuntoView, 'protocolo_llamadas')

urlpatterns = [
    path('render', views.render_template_base),
    path('', views.index),
    path('api/get_all_puntos', views.get_all_puntos, name='get_all_puntos'),
    path('api/contesto/<int:id>', views.contesto, name='contesto'),
    path('api/no_contesto/<int:id>', views.no_contesto, name='contesto'),
    path('api/edit/<int:id>', views.edit, name='contesto'),
    path('api/llamando/<int:id>', views.llamando, name='llamando'),

    path('historico', views.historico, name='historico'),
    # path('api_v1/llamando', views.llamando, 'llamando'),
    path('api/', include(router.urls)),
]