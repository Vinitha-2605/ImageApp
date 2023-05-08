from django.urls import path
from . import views

urlpatterns = [
    path('image', views.upload),
    path('category', views.addcategory),
    path('imagedetail/<id>', views.imagedetail, name="details"),
    path("imageview", views.imageview, name="view"),
    path('search', views.searchimage, name = "filter"),
    path('searchcategory', views.searchcategory, name="search")
]