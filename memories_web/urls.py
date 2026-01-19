
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("memories.urls")),
    path('user/', include("users.urls")),
    path('accounts/', include('allauth.urls')),
]
