import allure

from a10_appium_auto.base.base_action import BaseAction

from selenium.webdriver.common.by import By


class SettingPage(BaseAction):
    more_button = By.XPATH, "//*[@text='更多']"
    search_button = By.ID, "com.android.settings:id/search"

    # 点击更多
    @allure.step(title="点击更多")
    def click_more(self):
        self.click(self.more_button)

    # 点击搜索
    @allure.step(title="点击搜索")
    def click_search(self):
        self.click(self.search_button)
