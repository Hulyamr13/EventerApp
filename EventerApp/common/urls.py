from django.urls import path

from EventerApp.common.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
