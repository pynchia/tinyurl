from behave import *
from short.models import Entry


@given(u'the short URL id "{url_id}" exists')
def step_impl(context, url_id):
    context.entry = Entry.objects.get(id=url_id)


@when(u'I ask for the stats of short URL "{short_url}"')
def step_impl(context, short_url):
    context.browser.get(short_url)
    assert False


@then(u'the page will show the stats of short URL id "{url_id}"')
def step_impl(context, url_id):
    assert False
# -------------


@then(u'the page will show an error about short URL id "{url_id}"')
def impl(context):
    assert False

