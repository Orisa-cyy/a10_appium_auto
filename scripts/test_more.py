import time

from a10_appium_auto.base.base_driver_setting import init_driver_setting
from ..page.page import Page


class TestMore:
    def setup(self):
        self.driver = init_driver_setting()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    def test_more_2g(self):
        self.page.setting.click_more()
        self.page.more.click_mobile_network()
        self.page.mobile_network.click_first_network()
        self.page.mobile_network.click_network_2g()

    def test_more_3g(self):
        self.page.setting.click_more()
        self.page.more.click_mobile_network()
        self.page.mobile_network.click_first_network()
        self.page.mobile_network.click_network_3g()
