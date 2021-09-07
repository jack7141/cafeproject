from django.urls import path
from cafes import views as CafeViews

app_name = "core"

urlpatterns = [path("", CafeViews.HomeView.as_view(), name="CoreHomeView")]