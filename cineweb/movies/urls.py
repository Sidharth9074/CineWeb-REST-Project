from django.urls import path

from . import views

urlpatterns = [

    path('movies/',views.MovieListCreateView.as_view()),

    path('movies/<str:uuid>/',views.MovieRetrieveUpdateDestroyView.as_view()),

    path('industry/',views.IndustryListCreateView.as_view()),

    path('director/',views.DirectorListCreateView.as_view()),
    
    path('genre/',views.GenreListCreateView.as_view()),

    path('recommended-movies/<str:uuid>/',views.RecommendedMoviesView.as_view()),



    
]