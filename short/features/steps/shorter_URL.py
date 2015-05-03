from behave import *
from short.models import Entry

url1 = 'https://docs.djangoproject.com/en/dev/ref/models/querysets/#django.db.models.query.QuerySet.create'


@given(u'I go the the homepage')
def go_to_homepage(context):
    context.browser.get(context.server_url)
    assert "URL shortener" in context.browser.title


@when(u'I post the URL in the form')
def post_long_url(context):
    context.browser.find_element_by_id('id_url').send_keys(url1)
    context.browser.find_element_by_id('submit').click()


@then(u'I will see the resulting shorter URL')
def see_short_url(context):
    entry = Entry.objects.get(url=url1)
    context.browser.find_element_by_link_text(
            'http://localhost:8081/r/%d/' % entry.id)

