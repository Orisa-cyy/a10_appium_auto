import allure

from a10_appium_auto.base.base_action import BaseAction

from selenium.webdriver.common.by import By


class MorePage(BaseAction):
    mobile_network_button = By.XPATH, "//*[@text='移动网络']"

    # 点击移动网络
    @allure.step(title="点击移动网络")
    def click_mobile_network(self):
        self.click(self.mobile_network_button)
