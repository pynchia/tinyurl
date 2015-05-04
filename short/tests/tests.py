from django.test import TestCase
from django.core.urlresolvers import reverse
from short.models import Entry

# Create your tests here.


class MyTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.url1 = 'https://www.python.org/dev/peps/pep-0020/'
        cls.entry1 = Entry.objects.create(url=cls.url1)

        cls.url2 = 'https://docs.djangoproject.com/en/dev/topics/testing/tools/'
        cls.entry2 = Entry.objects.create(url=cls.url2)

        cls.url3 = 'http://stackoverflow.com/questions/tagged/python'

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

    def test_posturl_once(self):
        response = self.client.post(reverse('short:home'),
                                    data={'url': self.url3},
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.url3, response.content)

    def test_post_sameurl_twice(self):
        self.client.post(reverse('short:home'),
                         data={'url': self.url3})
        response = self.client.post(reverse('short:home'),
                                    data={'url': self.url3})
        self.assertEqual(response.status_code, 200)
        self.assertIn('That URL has been shortened already',
                      response.content)

    def test_show_url(self):
        # get the first one
        response = self.get_page_200('short:showurl',
                                     kwargs={'pk': self.entry1.id})
        self.assertIn(self.entry1.url, response.content)

        # cannot test external redirects. Use BDD instead

    def test_redirect_fails(self):
        #if the short url has not been created yet, redirect to homepage
        response = self.client.get('http://localhost:8081/r/666/')
        self.assertRedirects(response, reverse('short:home'))

    def test_url_hits(self):
        self.fail('not over yet')

