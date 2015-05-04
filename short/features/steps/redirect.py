from behave import *

url1 = 'https://docs.djangoproject.com/en/dev/topics/testing/tools/'


@given(u'I have obtained a short URL already')
def obtain_short_url(context):
    context.browser.get(context.HOMEPAGE)
    context.browser.find_element_by_id('id_url').send_keys(url1)
    context.browser.find_element_by_id('submit').click()


@when(u'I use the short URL (e.g. clicking on a link)')
def access_short_url(context):
    context.browser.find_element_by_id('id_short_url').click()


@then(u'I will be redirected to the original URL')
def redirected_to_original_url(context):
    assert context.browser.current_url == url1
# ---------------


@when(u'I access the missing short URL via web')
def access_missing_short_url_web(context):
    context.browser.get('http://localhost:8081/r/666/')


@then(u'I will be redirected to the home page')
def redirected_to_homepage(context):
    assert context.browser.current_url == context.HOMEPAGE
# ---------------


@when(u'I access the missing short URL via REST')
def access_missing_short_url_rest(context):
    assert False


@then(u'I will receive an error')
def receive_an_error_rest(context):
    assert False

