from django.urls import path

# from .views import home, about

from demo_app import views

urlpatterns = [
    # path("home/", home, name="home"),
    path("home/", views.home, name="home"),
    # path("about/", about, name="about"),
    path("about/", views.about, name="about"),
]
