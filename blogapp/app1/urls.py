from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('login/',views.login),
    path('login1/',views.login1),
    path('signup/',views.signup),
    path('signup1/',views.Signedup.as_view()),
    path('logout/',views.logout),
]