#import time
from behave import *
from urlparse import urlsplit
from short.models import Entry


@given(u'the set of URLs are added to the DB')
def impl(context):
    for row in context.table:
        entry = Entry.objects.create(url=row['url'])


@given(u'"{long_url}" has a short URL')
def step_impl(context, long_url):
    context.entry = Entry.objects.get(url=long_url)


@given(u'"{long_url}" has no short url')
def step_impl(context, long_url):
    try:
        Entry.objects.get(url=long_url)
    except Entry.DoesNotExist:
        pass
    else:
        assert False, "url % exists already" % long_url


@given(u'the short URL id "{url_id}" exists')
def step_impl(context, url_id):
    context.entry = Entry.objects.get(id=url_id)


@given(u'the short URL id "{url_id}" is missing')
def step_impl(context, url_id):
    try:
        Entry.objects.get(id=url_id)
    except Entry.DoesNotExist:
        pass
    else:
        assert False, "short url with id=% exists already" % url_id


@when(u'I go to the homepage')
def step_impl(context):
    context.browser.get(context.HOMEPAGE)


@when(u'I go to the page "{url}"')
def step_impl(context, url):
    context.browser.get(url)


@when(u'I use the short URL of long URL "{long_url}"')
def step_impl(context, long_url):
    entry = Entry.objects.get(url=long_url)
    context.browser.get(entry.get_link())


@then(u'I will be redirected to "{long_url}"')
def step_impl(context, long_url):
    assert context.browser.current_url == long_url, "%s **vs** %s" % (context.browser.current_url, long_url)


@then(u'the page shows a form for creating a new short URL')
def impl(context):
    context.browser.find_element_by_name('id_create_form')


@then(u'the page shows a form for searching existing URLs')
def impl(context):
    context.browser.find_element_by_id('id_search_form')


@when(u'I post "python" in the search form')
def impl(context):
    assert False


@then(u'the page will show "{num_entries}" entries containing "{keyword}"')
def impl(context):
    assert False


@then(u'each entry will show a link to its stats page')
def impl(context):
    assert False


@when(u'I post "{long_url}" in the homepage form')
def step_impl(context, long_url):
    context.browser.get(context.HOMEPAGE)
    context.browser.find_element_by_id('id_url').send_keys(long_url)
    context.browser.find_element_by_id('submit').click()


@then(u'the page will show the short URL for "{long_url}"')
def step_impl(context, long_url):
    entry = Entry.objects.get(url=long_url)
    context.browser.find_element_by_link_text(entry.get_link())


@then(u'the number of hits of the long URL "{long_url}" will be "{num_hits}"')
def step_impl(context, long_url, num_hits):
    entry = Entry.objects.get(url=long_url)
    assert str(entry.num_hits) == num_hits


@then(u'I will be redirected to the homepage')
def step_impl(context):
    assert context.browser.current_url == context.HOMEPAGE


@then(u'the page will show the stats of short URL id "{url_id}"')
def step_impl(context, url_id):
    context.browser.find_element_by_id('id_short_url')
    num_hits_on_page = context.browser.find_element_by_id('id_num_hits').text
    assert (num_hits_on_page == str(context.entry.num_hits)), "%s ***vs*** %s" % (num_hits_on_page, str(context.entry.num_hits))


@then(u'the page will show an error about short URL "{short_url}"')
def impl(context, short_url):
    short_url_path = urlsplit(short_url).path
    assert short_url_path == context.browser.find_element_by_id('id_error').text

