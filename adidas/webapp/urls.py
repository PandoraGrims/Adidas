from django.urls import path

from webapp.views import AdidasListView

app_name = "webapp"

urlpatterns = [
    path('', AdidasListView.as_view(), name="index"),
]
