from django.urls import include,path
from movieAPI.views import MovieListView,AddMovie,RegisterUser,RatingMovie
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('movieAPI/movies',MovieListView.as_view(),name="MovieListView"),
    path('movieAPI/AddMovie/<int:pk>',AddMovie.as_view(),name="AddMovie"),
    path('movieAPI/RateMovie/<int:pk>',RatingMovie.as_view(),name = "RatingMovie"),
    path('movieAPI/RegisterUser',RegisterUser.as_view(),name="RegisterUser"),
    path('movieAPI/Login',obtain_auth_token,name="ObtainToken")
]