from django.conf.urls import include, url

from pay.views import pay, check_pay, index
from project.views import *

urlpatterns = [
    url(r"^$", index),
    url(r"^pay/$", pay),
    url(r"^check_pay/$", check_pay),
]