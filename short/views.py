# from django import http
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic

from .models import Entry
from .forms import EntryForm, SearchForm


# Create your views here.
class HomePageView(generic.CreateView):
    model = Entry
    form_class = EntryForm
    template_name = "short/home.html"

    def get_success_url(self):
        return reverse_lazy('short:showurl', kwargs={'pk': self.object.id})


class SearchURLView(generic.edit.FormMixin, generic.ListView):
    form_class = SearchForm
    template_name = 'short/searchurl.html'
    context_object_name = 'matching_urls'
    paginate_by = Entry.NUM_ENTRIES_PER_PAGE

    def get_form_kwargs(self):
        "need to redefine it since it works with POST,PUT only"
        return {'initial': self.get_initial(),
                'prefix': self.get_prefix(),
                'data': self.request.GET}

    def get_queryset(self):
        # only is_valid is necessary if url field is req
        if self.form.is_valid() and self.request.GET.get('substring', None) is not None:
            return Entry.objects.filter(**self.form.filter_by())
        # otherwise an empty queryset
        return Entry.objects.none()

    def get(self, *args, **kwargs):
        # if I assign it to the view instance it appears in the context
        # under view (i.e. get_context_data adds the view to the context)
        self.form = self.get_form(self.get_form_class())
        return super(SearchURLView, self).get(*args, **kwargs)


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
