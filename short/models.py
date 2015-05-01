from django.db import models


class Entry(models.Model):
    # the long url given
    url = models.URLField(help_text='the one you want to shorten')
    # the short url is going to be the pk itself
    # so no other field is necessary now

    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    # how many times the short url was used
    num_hits = models.IntegerField(default=0, editable=False)

    def __unicode__(self):
        return u'%d' % self.id

