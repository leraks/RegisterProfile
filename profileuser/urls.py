from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name="profile"),
    path('profile_edit/', views.edit_profile, name="profile_edit"),

]