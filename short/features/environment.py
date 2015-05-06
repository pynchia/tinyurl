from selenium import webdriver
# from short.models import Entry


def before_all(context):
    context.browser = webdriver.Firefox()
    context.browser.implicitly_wait(3)
    context.HOMEPAGE = 'http://localhost:8081/'

#    Entry.objects.create(
#                    url="http://pythonhosted.org/behave/tutorial.html#python-step-implementations")
#    Entry.objects.create(
#                    url="http://selenium-python.readthedocs.org/en/latest/getting-started.html")


def after_all(context):
    context.browser.quit()


def before_feature(context, feature):
    pass
