import unittest

from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has started a cool new online to do app.
        # She goes to check out its homepage
        self.browser.get("http://localhost:8000")

        # She notices the page title and header mention to do lists
        self.assertIn("To-Do", self.browser.title)
        self.fail("Finish the test!")
        # He is invited to enter a to do item straight away

        # He types "Buy oat milk" into a text box

        # When he hits enter, the page updates and now the page lists
        # "1: Buy oat milk" as an item in a to do list

        # There is still a text box inviting him to add another item.
        # He enters "Use Oat milk in Protein shake"

        # The page updates again and now shows both items on his list

        # He wonders whether the site will remember the list. Then he sees
        # That the site has generated a unique URL for him. There is some
        # explanatory text to that effect.
        # He visits that URL. His to do list is still there.


if __name__ == "__main__":
    unittest.main(warnings="ignore")
