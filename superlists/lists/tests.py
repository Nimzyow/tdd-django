from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from django.urls import resolve
from lists.models import Item
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

    def test_uses_home_template(self):
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

    def test_only_saves_item_when_necessary(self):
        self.client.get("/")
        self.assertEqual(Item.objects.count(), 0)

    def test_can_save_a_POST_request(self):
        self.client.post("/", data={"item_text": "A new list item"})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, "A new list item")

    def test_redirects_after_POST(self):
        response = self.client.post("/", data={"item_text": "A new list item"})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response["location"], "/lists/the-only-list-in-the-world"
        )

    def test_displays_all_list_items(self):
        Item.objects.create(text="item 1")
        Item.objects.create(text="item 2")

        response = self.client.get("/")

        self.assertIn("item 1", response.content.decode())
        self.assertIn("item 2", response.content.decode())


class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = "The first (ever) list item"
        first_item.save()

        second_item = Item()
        second_item.text = "Item the second"
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual("The first (ever) list item", first_saved_item.text)
        self.assertEqual("Item the second", second_saved_item.text)


class LiveViewTest(TestCase):
    def test_displays_all_items(self):
        Item.objects.create(text="item 1")
        Item.objects.create(text="item 2")

        response = self.client.get("/lists/the-only-list-in-the-world")
        '''
            Here's a new helper method: instead of using the slightly annoying
            assertIn/response.content.decode() dance, Django provides the
            assertContains method, which knows how to deal with responses and
            the bytes of their content.
        '''
        self.assertContains(response, "item 1")
        self.assertContains(response, "item 2")
