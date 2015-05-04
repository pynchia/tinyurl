from behave import *
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

