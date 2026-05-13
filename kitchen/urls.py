from django.urls import path

from kitchen.views import index, signup

urlpatterns = [
    path("", index, name="index"),
    path("signup/", signup, name="signup"),
]

app_name = "kitchen"
