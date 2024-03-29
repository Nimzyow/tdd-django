from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from django.urls import resolve
from lists.views import home_page


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        '''
        resolve is the function Django uses internally to resolve
        URLs and find what view function they should map to.  We're checking that
        resolve, when called with “/”, the root of the site, finds a function
        called home_page.
        '''

        found = resolve("/")
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        # request = HttpRequest()
        # response = home_page(request)
        '''
        Instead of manually creating an HttpRequest object and calling the view
        function directly, we call self.client.get, passing it the URL we want
        to test.
        '''
        response = self.client.get("/")
        # below are old assertions
        # html = response.content.decode("utf8")
        # self.assertTrue(html.startswith("<html>"))
        # self.assertIn("<title>To-Do lists</title>", html)
        # self.assertTrue(html.endswith("</html>"))

        self.assertTemplateUsed(response, "home.html")
