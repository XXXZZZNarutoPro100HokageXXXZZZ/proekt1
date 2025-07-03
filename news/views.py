from sre_parse import SUCCESS
from django.shortcuts import render
from django.http import HttpResponse
from .models import novost
from django.views.generic import UpdateView, DeleteView
from main.forms import novostForm

def news_home(request):
    news = novost.objects.all()
    return render(request,'news/news.html',{'news':news})

def news_detail(request, pk):
    post = novost.objects.get(pk=pk)
    return render(request, 'news/news_detail.html', {'post': post})

class NewsUpdateView(UpdateView):
    model = novost
    success_url = '/news/'
    template_name = 'main/create.html'
    form_class = novostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_update'] = True
        return context

class NewsDeleteView(DeleteView):
    model = novost
    success_url = '/news/'
    template_name = 'news/news_delete.html'