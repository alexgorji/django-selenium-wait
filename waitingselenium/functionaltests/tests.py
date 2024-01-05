from selenium.webdriver.common.by import By

from django.urls import reverse

from functionaltests.base import FunctionalTest


class TestWait(FunctionalTest):
    def test_scroll_down_and_wait(self):
        self.driver.get(f"{self.live_server_url}{reverse('demo')}")
        self.driver.maximize_window()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.driver.find_element(By.CSS_SELECTOR, "input[value='Save']").click()
