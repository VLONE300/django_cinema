from django.urls import path

from cinema.views import MovieListView, MovieDetailView, BuyTicketView

urlpatterns = [
    path('', MovieListView.as_view(), name='movie-list'),
    path('movie/<int:movie_id>/', MovieDetailView.as_view(), name='movie_detail'),
    path('movie/<int:show_id>/buy_ticket', BuyTicketView.as_view(), name='buy-ticket'),
]
