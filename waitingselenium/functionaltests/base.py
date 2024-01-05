import os

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self) -> None:
        headless = os.getenv('HEADLESS', default='True')
        chrome_options = Options()
        if headless not in ('False', 'false'):
            chrome_options.add_argument("--headless=new")
        self.driver = webdriver.Chrome(options=chrome_options)
        super().setUp()

    def tearDown(self) -> None:
        self.driver.quit()
        super().tearDown()
