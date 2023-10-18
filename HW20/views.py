from django.views.generic import ListView, DetailView
from .models import Article

class ArticleListView(ListView):
    model = Article
    template_name = 'HW20/article_list.html'

    def get_queryset(self):
        return Article.objects.all().order_by('-created_at') 

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'HW20/article_detail.html'
