from django.shortcuts import render
from django.urls import reverse_lazy
from app.models import Child, Report
from django.views.generic import TemplateView, ListView, CreateView, DetailView
from django.views.generic.edit import FormView, UpdateView
from app.forms import PinForm



#class IndexView(TemplateView):
#    template_name = "index.html"


class PinView(FormView):
    template_name = 'index.html'
    form_class = PinForm
    success_url = reverse_lazy('report_create_view' )

    def form_valid(self, form):
        return super(PinView, self).form_valid(form)


class ReportCreateView(CreateView):
    model = Report
    fields = ('child_status',)
    success_url = reverse_lazy('pin_view')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.child = Child.objects.get(id=1)
        return super().form_valid(form)

class ChildListView(ListView):
    template_name = "child_list.html"
    model = Child


class ChildCreateView(CreateView):
    model = Child
    fields = ('first_name', 'last_name', 'middle_initial', 'pin',)
    success_url = reverse_lazy('child_list_view')


    def form_valid(self, form):
        instance = form.save(commit=False)

        return super().form_valid(form)

class ChildUpdateView(UpdateView):

    model = Child
    fields = ('first_name', 'last_name', 'middle_initial', 'pin',)
    success_url = reverse_lazy('child_list_view')
