from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from app.models import Child, Report
from django.views.generic import TemplateView, ListView, CreateView, DetailView
from django.views.generic.edit import FormView, UpdateView
from app.forms import PinForm
from hashids import Hashids




#class IndexView(TemplateView):
#    template_name = "index.html"


class PinView(FormView):
    template_name = 'index.html'
    form_class = PinForm

    def form_valid(self, form):
        try:
            return super(PinView, self).form_valid(form)
        except ValueError:
            return super(PinView, self).form_invalid(form)
    def get_success_url(self):
        hashids = Hashids().encode(int(self.request.POST['pin']))
        print(hashids)
        return reverse('report_create_view', args=[hashids])


class ReportCreateView(CreateView):
    model = Report
    fields = ('child_status',)
    success_url = reverse_lazy('pin_view')

    def form_valid(self, form):
        instance = form.save(commit=False)
        pin = Hashids().decode(self.kwargs['pin'])
        instance.child = Child.objects.get(pin=pin[0])
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
