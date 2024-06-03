from core.views import Home, ProfilesList,ProfileCreate,watch,ShowMovieDetail,ShowMovie
from django.urls import path

app_name = 'core'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('profile/', ProfilesList.as_view(), name='profile_list'),
    path('Profile/create',ProfileCreate.as_view(),name="profile_create"),
    path('watch/<str:profile_id>/', watch.as_view(), name='watch'),
    path('movie/detail/<str:movie_id>',ShowMovieDetail.as_view(), name="show_det"),
    path('movie/play/<str:movie_id>',ShowMovie.as_view(),name="play")

]
