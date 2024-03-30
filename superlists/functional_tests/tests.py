import time
import unittest

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

MAX_WAIT = 10


class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element(By.ID, "id_list_table")
                rows = table.find_elements(By.TAG_NAME, "tr")
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has started a cool new online to do app.
        # She goes to check out its homepage
        self.browser.get(self.live_server_url)

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

        self.wait_for_row_in_list_table("1: Buy oat milk")

        # There is still a text box inviting him to add another item.
        # He enters "Use Oat milk in Protein shake"
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        inputbox.send_keys("Use Oat milk in protein shake")
        inputbox.send_keys(Keys.ENTER)

        # The page updates again and now shows both items on his list

        self.wait_for_row_in_list_table("1: Buy oat milk")
        self.wait_for_row_in_list_table("2: Use Oat milk in protein shake")

        # self.fail("Finish the test!")

        # He wonders whether the site will remember the list. Then he sees
        # That the site has generated a unique URL for him. There is some
        # explanatory text to that effect.
        # He visits that URL. His to do list is still there.

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Nima starts a new To Do list
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        inputbox.send_keys("Buy shoes")
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Buy shoes")

        # He notices that his list has a unique URL
        nima_list_url = self.browser.current_url
        self.assertRegex(nima_list_url, '/lists/.+')

        # Now a new user, Francies, comes along to the site

        # We use a new browser session to make sure that no information
        # of Nimas is coming through from cookies
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francies visits the new home page. No sign on Nimas list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element(By.TAG_NAME, "body").text
        self.assertNotIn("Buy shoes", page_text)
        self.assertNotIn("Use Oat milk in protein shake", page_text)

        # Francis starts a new list by entering a new item
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        inputbox.send_keys("Buy milk")
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Buy milk")
