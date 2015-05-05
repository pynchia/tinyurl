# from django import http
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


class ShowURLView(generic.TemplateView):
    template_name = "short/showurl.html"

    def get_context_data(self, **kwargs):
        context = super(ShowURLView, self).get_context_data(**kwargs)
        try:
            entry = Entry.objects.get(pk=kwargs['pk'])
        except Entry.DoesNotExist:
            pass
        else:
            context.update({'short_url': entry.get_link(),
                            'entry': entry})
        return context


class RedirectToURLView(generic.RedirectView):
    # it should be True, so the browser can go straight to it next time
    permanent = False

    # TBD find out what method gets the destination
    def get_redirect_url(self, pk):
        try:
            entry = Entry.objects.get(pk=pk)
        except Entry.DoesNotExist:
            return reverse('short:home')
        else:
            entry.num_hits += 1
            entry.save()
            return entry.url
