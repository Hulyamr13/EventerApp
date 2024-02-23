from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("EventerApp.common.urls")),
    path('', include("EventerApp.events.urls")),
    path('profile/', include("EventerApp.accounts.urls")),
]
