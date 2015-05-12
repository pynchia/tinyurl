from django.db import models
from django.conf import settings


class Entry(models.Model):

    NUM_ENTRIES_PER_PAGE = 4

    # the long url given
    # url = models.URLField(unique=True,
    url = models.URLField(help_text='the URL you want to shorten')
    # the short url is going to be the id itself
    # so no other field is necessary now

    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    # how many times the short url was used
    num_hits = models.IntegerField(default=0, editable=False)

    def get_link(self):
        "returns the html link for the short URL"
        link = '%s/r/%d/' % (settings.SITE_URL, self.id)
        return link

    def get_absolute_url(self):
        # TBC can I use rf's reverse('entry-detail', args=(self.id,), request)
        return '%s/api/entries/%d/' % (settings.SITE_URL, self.id)

    def __unicode__(self):
        return u'%d' % self.id
