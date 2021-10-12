from django.urls import path
from cafes import views as CafeViews

app_name = "core"

urlpatterns = [
    path("", CafeViews.HomeView.as_view(), name="CoreHomeView"),
    path("city/<str:county>/", CafeViews.CityDetail.as_view(), name="CityHomeView"),
]