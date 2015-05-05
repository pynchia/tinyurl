from behave import *
from urlparse import urlsplit
from short.models import Entry


@given(u'"{long_url}" has no short url')
def step_impl(context, long_url):
    try:
        Entry.objects.get(url=long_url)
    except Entry.DoesNotExist:
        pass
    else:
        assert False, "url % exists already" % long_url


@when(u'I post "{long_url}" in the homepage form')
def step_impl(context, long_url):
    context.browser.get(context.HOMEPAGE)
    context.browser.find_element_by_id('id_url').send_keys(long_url)
    context.browser.find_element_by_id('submit').click()


@then(u'the page will show the short URL for "{long_url}"')
def step_impl(context, long_url):
    entry = Entry.objects.get(url=long_url)
    context.browser.find_element_by_link_text(entry.get_link())


@given(u'"{long_url}" has a short url')
def step_impl(context, long_url):
    context.entry = Entry.objects.get(url=long_url)


@when(u'I use the short URL "{short_url}"')
def step_impl(context, short_url):
    context.browser.get(short_url)


@then(u'I will be redirected to "{long_url}"')
def step_impl(context, long_url):
    assert context.browser.current_url == long_url


@then(u'the number of hits of the short URL id "{url_id}" will increase')
def step_impl(context, url_id):
    "it expects to find a context.entry obj"
    context.browser.get("http://localhost:8081/showurl/%s/" % url_id)
    num_hits_on_page = context.browser.find_element_by_id('id_num_hits').text
    assert (num_hits_on_page == str(context.entry.num_hits+1)), "%s ***vs*** %s" % (num_hits_on_page, str(context.entry.num_hits))


@given(u'the short URL id "{url_id}" is missing')
def step_impl(context, url_id):
    try:
        Entry.objects.get(id=url_id)
    except Entry.DoesNotExist:
        pass
    else:
        assert False, "short url with id=% exists already" % url_id


@then(u'I will be redirected to the home page')
def step_impl(context):
    assert context.browser.current_url == context.HOMEPAGE


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


@then(u'the page will show an error about short URL "{short_url}"')
def impl(context, short_url):
    short_url_path = urlsplit(short_url).path
    assert short_url_path == context.browser.find_element_by_id('id_error').text

