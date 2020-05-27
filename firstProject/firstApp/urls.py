from django.urls import path
from firstApp.views import display
from firstApp.views import displayDateTime

urlpatterns = [
    path('hello/', display),
    path('datetime/', displayDateTime)
]
