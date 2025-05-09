from django.urls import path
from .views import search_view  # On importe notre fonction de vue

urlpatterns = [
    path('search/', search_view, name='search'),  # Quand on va à /search/, Django appelle search_view

]
