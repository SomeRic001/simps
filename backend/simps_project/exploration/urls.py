from django.urls import path
from . import views

app_name = "explore"

urlpatterns = [
    path("", views.explore_home, name="home"),
    path("buy/", views.buy_equity, name="buy_equity"),
]