from selenium import webdriver
from short.models import Entry


def before_all(context):
    context.browser = webdriver.Firefox()
    context.browser.implicitly_wait(3)
    context.HOMEPAGE = 'http://localhost:8081/'

    entry = Entry.objects.create(
                    url="http://stackoverflow.com/questions/tagged/python")
    # context.exist_entry_id = entry.id


def after_all(context):
    context.browser.quit()


def before_feature(context, feature):
    pass
