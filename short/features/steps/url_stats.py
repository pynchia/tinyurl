from urlparse import urlsplit
from behave import *
from short.models import Entry


@given(u'the short URL id "{url_id}" exists')
def step_impl(context, url_id):
    context.entry = Entry.objects.get(id=url_id)


@when(u'I ask for the stats of short URL "{short_url}"')
def step_impl(context, short_url):
    context.browser.get(short_url)


@then(u'the page will show the stats of short URL id "{url_id}"')
def step_impl(context, url_id):
    context.browser.find_element_by_id('id_short_url')
    num_hits_on_page = context.browser.find_element_by_id('id_num_hits').text
    assert (num_hits_on_page == str(context.entry.num_hits)), "%s ***vs*** %s" % (num_hits_on_page, str(context.entry.num_hits))
# -------------


@then(u'the page will show an error about short URL "{short_url}"')
def impl(context, short_url):
    short_url_path = urlsplit(short_url).path
    assert short_url_path == context.browser.find_element_by_id('id_error').text

