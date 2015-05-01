from django.test import TestCase
from django.core.urlresolvers import reverse
from short.models import Entry

# Create your tests here.


class MyTestCase(TestCase):
    # fixtures = ['xyz', ]

    # def setUp(self):
    #     pass

    # def tearDown(self):
    #     pass

    def get_page_200(self, pagename, kwargs=None):
        "Utility function to get a page and check the response is OK"
        response = self.client.get(reverse(pagename, kwargs=kwargs))
        # the page exists and is returned
        self.assertEqual(response.status_code, 200)
        return response

    def test_get_home_page(self):
        self.get_page_200('short:home')

