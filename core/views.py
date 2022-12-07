from django.shortcuts import render
from django.views.generic import FormView, TemplateView, ListView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ContatoForm
from .models import Post

def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts':posts})

class IndexView(FormView):
    template_name = 'index.html'
    
    form_class = ContatoForm
    success_url = reverse_lazy('index')
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context
    
    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, "E-mail enviado com sucesso")
        return super(IndexView, self).form_valid(form, *args, **kwargs)
    
    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, "Erro ao enviar e-mail")
        return super(IndexView, self).form_invalid(form, *args, **kwargs)

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
