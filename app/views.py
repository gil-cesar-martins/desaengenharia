from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Post

def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts':posts})

class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['post'] = Post.objects.all()
        return context

class PortfolioDetails1View(TemplateView):
    template_name = 'portfolio-details1.html' 

class PortfolioDetails2View(TemplateView):
    template_name = 'portfolio-details2.html' 

class PortfolioDetails3View(TemplateView):
    template_name = 'portfolio-details3.html'

class PortfolioDetails4View(TemplateView):
    template_name = 'portfolio-details4.html'

class PortfolioDetails5View(TemplateView):
    template_name = 'portfolio-details5.html'

class PortfolioDetails6View(TemplateView):
    template_name = 'portfolio-details6.html'

class PortfolioDetails7View(TemplateView):
    template_name = 'portfolio-details7.html'

class PortfolioDetails2View(TemplateView):
    template_name = 'portfolio-details2.html'

class PortfolioDetails8View(TemplateView):
    template_name = 'portfolio-details8.html'

class PortfolioDetails9View(TemplateView):
    template_name = 'portfolio-details9.html'

class PortfolioDetails10View(TemplateView):
    template_name = 'portfolio-details10.html'

class PortfolioDetails11View(TemplateView):
    template_name = 'portfolio-details11.html'

class PortfolioDetails12View(TemplateView):
    template_name = 'portfolio-details12.html'

class BlogView(ListView):
    model = Post
    template_name = 'blog.html' 

class BlogSingleView(DetailView):
    model = Post
    template_name = 'blog-single.html' 

