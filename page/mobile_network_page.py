import allure

from a10_appium_auto.base.base_action import BaseAction

from selenium.webdriver.common.by import By


class MobileNetworkPage(BaseAction):
    first_network_button = By.XPATH, "//*[@text='首选网络类型']"
    network_2g_button = By.XPATH, "//*[@text='2G']"
    network_3g_button = By.XPATH, "//*[@text='3G']"

    # 点击首选网络类型
    @allure.step(title="点击首选网络类型")
    def click_first_network(self):
        self.click(self.first_network_button)

    # 点击 2g
    @allure.step(title="点击2G")
    def click_network_2g(self):
        self.click(self.network_2g_button)

    # 点击 3g
    @allure.step(title="点击3G")
    def click_network_3g(self):
        self.click(self.network_3g_button)
