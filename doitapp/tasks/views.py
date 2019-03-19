"""Django libraries"""
from django.template import loader
from django.utils import timezone
from django.shortcuts import render, redirect
from django.http import Http404
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit  import UpdateView

"""Models"""
from .models import Task

class TasksFeedView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/feed.html'
    context_object_name = 'tasksList'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['summary']
    template_name_suffix = '_update_form'



    