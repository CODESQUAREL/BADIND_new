from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from articleapp.forms import ArticleCreationForm
from articleapp.models import Article

class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    success_url = reverse_lazy('articleapp:list')
    template_name = 'articleapp/create.html'
    
    def form_valid(self, form):
        form.instance.writer = self.request.user #request를 보내는 유저로 데이터베이스에 writer로 설정해준 것
        return super().form_valid(form)