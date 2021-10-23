from django.views.generic import CreateView
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Link
from .forms import LinkForm
# Create your views here.


def home(request):
    return render(request, 'dashboard/home.html', {})


class LinkCreate(CreateView):
    form_class = LinkForm
    success_url = reverse_lazy('dashboard:home')
    template_name = 'dashboard/home.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user

        return super(LinkCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Link.objects.order_by('id')

        return super(LinkCreate, self).get_context_data(**kwargs)
