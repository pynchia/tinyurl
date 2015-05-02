from django.core.urlresolvers import reverse_lazy
from django.views import generic
from .models import Entry
from .forms import EntryForm


# Create your views here.
class HomePageView(generic.CreateView):
    model = Entry
    form_class = EntryForm
    template_name = "short/home.html"
    success_url = reverse_lazy('showurl')


class ShowURLView(generic.DetailView):
    model = Entry
    template_name = "short/showurl.html"


class RedirectToURLView(generic.RedirectView):
    # it should be True, so the browser can go straight to it
    permanent = False

    # TBD find out what method gets the destination
    def get_pattern_name(self):
        pass
