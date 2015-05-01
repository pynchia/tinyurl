from django.core.urlresolvers import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django.views import generic
from .models import Entry


# Create your views here.
class HomePageView(generic.CreateView):
    model = Entry
    fields = ['url', ]
    template_name = "short/home.html"
    success_url = reverse_lazy('showurl')


class ShowURLView(generic.DetailView):
    model = Entry
    template_name = "short/showurl.html"


class RedirectToURLView(generic.RedirectView):

    # TBD find out what method gets the destination
    def get_pattern_name(self):
        pass
