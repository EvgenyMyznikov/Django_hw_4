from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf import settings
import phones.views

urlpatterns = [
	path('admin/', admin.site.urls),
	path('catalog/', phones.views.show_catalog),
	path('catalog/<slug:slug>/', phones.views.show_product),
	path('catalog/<sort>/', phones.views.show_catalog)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
