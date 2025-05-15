from django.urls import path
from .views import PageListView, PageDetailview, PageCreateView

pages_patterns =( 
    [
        path('', PageListView.as_view(), name='pages'),
        path('<int:pk>/<slug:page_slug>/', PageDetailview.as_view(),  name='page'),
        path('create/', PageCreateView.as_view(), name = 'create'),]
        
        , 'pages')