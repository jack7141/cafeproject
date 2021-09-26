from django.urls import path
from . import views

app_name = "cafes"

urlpatterns = [
    path("<int:id>", views.CafeDetail.as_view(), name="viewDetail"),
    path("search/", views.search, name="viewSearch")
]