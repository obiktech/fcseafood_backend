from django.urls import path
from .views import getotp,checkotp, verifyotp

urlpatterns =[
    path("getotp",getotp),
    path("checkotp",checkotp),
    path("verifyotp",verifyotp),
]