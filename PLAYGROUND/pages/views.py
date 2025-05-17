
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Page
from .forms import PageForm

# Create your views here.

class StaffRequieredMixin(object):
    """
    Este Mixin requerira que el usuario sea miembro del Staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequieredMixin, self).dispatch(request, *args, **kwargs)
    
class PageListView(ListView):
   model = Page

class PageDetailview(DetailView):
    model = Page

class PageCreateView(StaffRequieredMixin, CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages')

class PageUpdateView(StaffRequieredMixin, UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = "_update_form"
    success_url = reverse_lazy('pages:pages')
    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'
    
class PageDeleteView(StaffRequieredMixin, DeleteView):
    model = Page
    success_url = reverse_lazy("pages:pages")