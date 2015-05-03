from urlparse import urlsplit, urlunsplit
from django import forms
#from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe
from .models import Entry


class EntryForm(forms.ModelForm):
    
    class Meta:
        model = Entry
        fields = ['url', ]

    def clean_url(self):
        # remove redundant delimiters
        url = urlunsplit(urlsplit(self.cleaned_data['url']))
        try:
            entry = Entry.objects.get(url=url)
        except Entry.DoesNotExist:
            pass
        else:
            raise forms.ValidationError(
                            mark_safe(
                                'That URL has been shortened already: '+
                                entry.get_link()
                            )
                        )
            # raise forms.ValidationError(
            #         _('The URL has been shortened already: %(link)s'),
            #         code='invalid',
            #         params={'link': entry.getlink(), })
        return url

