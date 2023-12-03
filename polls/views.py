from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator

from .models import *

class CategoriesListView(DetailView):
    model = Category
    template_name = "categories.html"

    def get_context_data(self, **kwargs):
        category = kwargs.get('object')

        context = super().get_context_data(**kwargs)

        page_number = self.request.GET.get("page", 1)
        paginator = Paginator(News.objects.filter(maincategory__pk=category.pk).order_by('created_at'), 10)
        page_obj = paginator.get_page(page_number)

        context['categories'] = Category.objects.order_by('created_at')
        context['category'] = category
        context['news'] = page_obj
        return context

class HomePageListView(ListView):
    model = Category
    template_name = "index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        page_number = self.request.GET.get("page", 1)
        paginator = Paginator(News.objects.order_by('created_at'), 10)
        page_obj = paginator.get_page(page_number)

        context['categories'] = Category.objects.order_by('created_at')
        context['news'] = page_obj
        return context


class NewsDetailView(DetailView):
    model = News
    template_name = 'single-news.html'
    context_object_name = 'news'



