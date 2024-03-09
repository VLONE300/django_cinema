from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.context_processors import messages
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView

from cinema.models import Movie, Show, Ticket


# Create your views here.
class MovieListView(ListView):
    model = Movie
    queryset = Movie.objects.all()


class MovieDetailView(DetailView):
    model = Movie
    pk_url_kwarg = 'movie_id'

    def get_context_data(self, **kwargs):
        context = super(MovieDetailView, self).get_context_data(**kwargs)
        context['shows'] = Show.objects.filter(movie=self.object)
        return context


class BuyTicketView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        show_id = kwargs.get('show_id')  # предполагается, что ID сеанса передается в URL
        show = Show.objects.get(id=show_id)
        if show.available_seats > 0:
            # Создаем билет
            ticket = Ticket.objects.create(show=show, user=request.user)
            # Уменьшаем количество доступных мест
            show.available_seats -= 1
            show.save()
            # Перенаправляем пользователя на страницу с подтверждением
            return redirect('movie-list')
        else:
            messages.error(request, 'No ticket available')
