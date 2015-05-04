from behave import *
from short.models import Entry

url1 = 'https://docs.djangoproject.com/en/dev/ref/models/querysets/#django.db.models.query.QuerySet.create'


@given(u'I go the the homepage')
def go_to_homepage(context):
    context.browser.get(context.HOMEPAGE)
    assert "URL shortener" in context.browser.title


@when(u'I post the URL in the form')
def post_long_url_via_form(context):
    context.browser.find_element_by_id('id_url').send_keys(url1)
    context.browser.find_element_by_id('submit').click()


@then(u'I will see the resulting shorter URL')
def see_short_url(context):
    entry = Entry.objects.get(url=url1)
    context.browser.find_element_by_link_text(
                            entry.get_link())


# @given(u'I call the api properly')
# def call_API_properly(context):
#     pass


@when(u'I post the URL to the server')
def post_long_url_via_REST_API(context):
    assert False


@then(u'I will receive the resulting shorter URL')
def receive_short_url(context):
    assert False

