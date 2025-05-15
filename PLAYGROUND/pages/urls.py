from django.urls import path
from . import views
from .views import PageListView, PageDetailview

urlpatterns = [
    path('', PageListView.as_view(), name='pages'),
    path('<int:pk>/<slug:page_slug>/', PageDetailview.as_view(),  name='page'),
]