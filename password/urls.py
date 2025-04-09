from django.urls import path
from .views import generate_password, home, about

urlpatterns = [                                                                                                                                                                                                                   
  path("", home, name="Home"),                                                                                   
  path("generate-password/", generate_password, name="generate-password"),
  path("about/", about, name="About"),

]
