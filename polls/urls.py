from django.urls import path
from .views import *


urlpatterns = [
    path('', HomePageListView.as_view(), name='homepage'),
    path('<int:pk>/<str:slug>', NewsDetailView.as_view(), name='single-news'),
    path('<int:pk>/categories/<str:slug>', CategoriesListView.as_view(), name="categories-detail")



]