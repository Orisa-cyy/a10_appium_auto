import pytest
from appium import webdriver
import time

from a10_appium_auto.base.base_driver_setting import init_driver_setting
from ..page.page import Page


class TestDisplay:
    def setup(self):
        self.driver = init_driver_setting()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_search(self):
        self.page.setting.click_search()
        self.page.search.input_search("蓝牙")
        self.page.search.click_back()
