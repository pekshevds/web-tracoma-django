from django.urls import path
from main_app.views import IndexView, AboutView

app_name = 'main_app'

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('about/', AboutView.as_view(), name="about"),
]
