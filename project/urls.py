from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from todo_api import urls as todo_urls

from test.views import index, health
# from . import views

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('todos/', include(todo_urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    try:
        import debug_toolbar
        urlpatterns += [path(r'__debug__', include(debug_toolbar.urls))]
    except ImportError:
        pass