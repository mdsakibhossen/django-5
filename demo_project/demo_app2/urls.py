from django.urls import path
from .views import contact
# from demo_app2 import views

urlpatterns = [
    path("contact/", contact, name="contact"),
    # path("contact/", views.contact, name="contact"),
]
