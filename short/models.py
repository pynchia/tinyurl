from django.db import models
from django.conf import settings

class Entry(models.Model):
    # the long url given
    # url = models.URLField(unique=True,
    url = models.URLField(
                          help_text='the URL you want to shorten')
    # the short url is going to be the id itself
    # so no other field is necessary now

    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    # how many times the short url was used
    num_hits = models.IntegerField(default=0, editable=False)

    def getlink(self):
        "returns the html link for the short URL"
        link = '%s/r/%d/' % (settings.SITE_URL, self.id)
        return '<a href="%s">%s</a>' % (link, link)

    def __unicode__(self):
        return u'%d' % self.id
