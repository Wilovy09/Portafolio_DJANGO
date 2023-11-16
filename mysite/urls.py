# django
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
# mios
from index import views
from contacto import views as contacto_views
from social import views as social_views
from proyectos import views as proyectos_views
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.index, name='index'),
    path('proyectos/', proyectos_views.proyectos, name='proyectos'),
    path('social/', social_views.social, name='social'),
    path('blog/', include('blog.urls'), name='blog'),
    path('contacto/', contacto_views.contacto, name='contacto'),
    path('contacto-whatsapp/', contacto_views.contacto_whats, name='contacto-whats'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'index.views.error404_view'