from django.urls import path

from .views import IndexView, PortfolioDetails1View, PortfolioDetails2View, PortfolioDetails3View, PortfolioDetails4View, PortfolioDetails5View, PortfolioDetails6View, PortfolioDetails7View, PortfolioDetails8View, PortfolioDetails9View, PortfolioDetails10View, PortfolioDetails11View, PortfolioDetails12View, BlogSingleView, BlogView 

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('portfolio-details1/', PortfolioDetails1View.as_view(), name='portfolio-details1'), 
    path('portfolio-details2/', PortfolioDetails2View.as_view(), name='portfolio-details2'), 
    path('portfolio-details2/', PortfolioDetails3View.as_view(), name='portfolio-details3'), 
    path('portfolio-details2/', PortfolioDetails4View.as_view(), name='portfolio-details4'), 
    path('portfolio-details2/', PortfolioDetails5View.as_view(), name='portfolio-details5'), 
    path('portfolio-details2/', PortfolioDetails6View.as_view(), name='portfolio-details6'), 
    path('portfolio-details2/', PortfolioDetails7View.as_view(), name='portfolio-details7'), 
    path('portfolio-details2/', PortfolioDetails8View.as_view(), name='portfolio-details8'), 
    path('portfolio-details2/', PortfolioDetails9View.as_view(), name='portfolio-details9'), 
    path('portfolio-details2/', PortfolioDetails10View.as_view(), name='portfolio-details10'), 
    path('portfolio-details2/', PortfolioDetails11View.as_view(), name='portfolio-details11'), 
    path('portfolio-details2/', PortfolioDetails12View.as_view(), name='portfolio-details12'), 
    path('blog-single/<int:pk>', BlogSingleView.as_view(), name='blog-single'), 
    path('blog/', BlogView.as_view(), name='blog'),
    
]