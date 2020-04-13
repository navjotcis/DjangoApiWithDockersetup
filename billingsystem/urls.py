from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('billingapp/', include('billingapp.urls')),
    path('webapp/', include('webapp.urls')),
]
