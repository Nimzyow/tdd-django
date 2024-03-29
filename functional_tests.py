import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


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

        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("To-Do", header_text)
        # He is invited to enter a to do item straight away

        inputbox = self.browser.find_element(By.ID, "id_new_item")
        self.assertEqual(
            inputbox.get_attribute("placeholder"),
            "Enter a to do item"
            )

        # He types "Buy oat milk" into a text box

        inputbox.send_keys("Buy oat milk")

        # When he hits enter, the page updates and now the page lists
        # "1: Buy oat milk" as an item in a to do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        self.assertTrue(
            any(row.text == "1: Buy oat milk" for row in rows),
            "New to do item did not appear in table"
        )

        # There is still a text box inviting him to add another item.
        # He enters "Use Oat milk in Protein shake"

        self.fail("Finish the test!")

        # The page updates again and now shows both items on his list

        # He wonders whether the site will remember the list. Then he sees
        # That the site has generated a unique URL for him. There is some
        # explanatory text to that effect.
        # He visits that URL. His to do list is still there.


if __name__ == "__main__":
    unittest.main(warnings="ignore")
