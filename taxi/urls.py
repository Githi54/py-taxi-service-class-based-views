from django.urls import path

from .views import index, ManufacturerListView

urlpatterns = [
    path("", index, name="index"),
    path("manufactures/", ManufacturerListView.as_view(), name="manufacturer-list")
]

app_name = "taxi"
