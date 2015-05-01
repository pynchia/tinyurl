from behave import *


@given(u'I go the the homepage')
def go_to_homepage(context):
    context.browser.get(context.server_url)
    assert "URL shortener" in context.browser.title


@when(u'I post the URL "{long_url}" in the form')
def post_long_url(context, long_url):
    context.browser.find_element_by_id('id_url').send_keys(long_url)
    context.browser.find_element_by_id('submit').click()
    assert False


@then(u'I will see the resulting shorter URL')
def see_short_url(context):
    assert False
