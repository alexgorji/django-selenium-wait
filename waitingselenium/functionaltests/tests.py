from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from django.urls import reverse
from selenium.webdriver.support.wait import WebDriverWait

from functionaltests.base import FunctionalTest


class TestWait(FunctionalTest):
    def test_do_not_scroll_down_and_wait(self):
        self.driver.get(f"{self.live_server_url}{reverse('demo_scrolldown')}")
        wait = WebDriverWait(self.driver, timeout=10)
        wait.until(lambda d: self.driver.find_element(By.CSS_SELECTOR, "input[value='Save']").is_displayed())
        self.driver.find_element(By.CSS_SELECTOR, "input[value='Save']").click()

    def test_do_not_scroll_down_and_wait_implicitly(self):
        self.driver.implicitly_wait(10)
        self.driver.get(f"{self.live_server_url}{reverse('demo_scrolldown')}")
        self.driver.find_element(By.CSS_SELECTOR, "input[value='Save']").click()

    def test_do_not_scroll_and_do_not_wait(self):
        self.driver.get(f"{self.live_server_url}{reverse('demo_scrolldown')}")
        self.driver.find_element(By.CSS_SELECTOR, "input[value='Save']").click()

    def test_scroll_down_and_wait(self):
        self.driver.get(f"{self.live_server_url}{reverse('demo_scrolldown')}")
        self.driver.maximize_window()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.driver.find_element(By.CSS_SELECTOR, "input[value='Save']").click()

    def test_wait_for_element_load(self):
        self.driver.get(f"{self.live_server_url}{reverse('demo_element_load')}")
        with self.assertRaises(NoSuchElementException):
            self.driver.find_element(By.CSS_SELECTOR, "input[value='Save']").click()
        wait = WebDriverWait(self.driver, timeout=10)
        wait.until(lambda d: self.driver.find_element(By.CSS_SELECTOR, "input[value='Save']").is_displayed())
        self.driver.find_element(By.CSS_SELECTOR, "input[value='Save']").click()

    def test_implicit_wait_for_element_load(self):
        self.driver.implicitly_wait(10)
        self.driver.get(f"{self.live_server_url}{reverse('demo_element_load')}")
        self.driver.find_element(By.CSS_SELECTOR, "input[value='Save']").click()
