from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView, DetailView
)
from django.urls import reverse_lazy

from .forms import BirthdayForm
from .models import Birthday
from .utils import calculate_birthday_countdown


class BirthdayDetailView(DetailView):
    model = Birthday

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['birthday_countdown'] = calculate_birthday_countdown(
            self.object.birthday
        )
        return context


class BirthdayListView(ListView):
    model = Birthday
    ordering = 'id'
    paginate_by = 10


class BirthdayCreateView(CreateView):
    model = Birthday
    form_class = BirthdayForm


class BirthdayUpdateView(UpdateView):
    model = Birthday
    form_class = BirthdayForm


class BirthdayDeleteView(DeleteView):
    model = Birthday
    success_url = reverse_lazy('birthday:list')
