from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from .models import Entry
from .forms import EntryForm


# Create your views here.
class HomePageView(generic.CreateView):
    model = Entry
    form_class = EntryForm
    template_name = "short/home.html"

    def get_success_url(self):
        return reverse_lazy('short:showurl', kwargs={'pk': self.object.id})


class ShowURLView(generic.DetailView):
    model = Entry
    template_name = "short/showurl.html"

    def get_context_data(self, **kwargs):
        context = super(ShowURLView, self).get_context_data(**kwargs)
        context['short_url'] = self.object.get_link()
        return context


class RedirectToURLView(generic.RedirectView):
    # it should be True, so the browser can go straight to it next time
    permanent = False

    # TBD find out what method gets the destination
    def get_redirect_url(self, pk):
        try:
            entry = Entry.objects.get(pk=pk)
        except Entry.DoesNotExist:
            # I should check if the request comes from a browser
            # if not then return an error instead of redirecting
            return reverse('short:home')
        else:
            return entry.url
