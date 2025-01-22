from django.contrib import admin
from django.urls import path, include
from Store import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/', include("Store.urls", namespace='Store')),
]

handler404 = views.handle_error_404