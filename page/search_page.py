import allure

from a10_appium_auto.base.base_action import BaseAction

from selenium.webdriver.common.by import By


class SearchPage(BaseAction):
    search_text = By.ID, "android:id/search_src_text"
    back_button = By.CLASS_NAME, "android.widget.ImageButton"

    # 搜索框输入
    @allure.step(title="搜索框输入")
    def input_search(self, content):
        self.input(self.search_text, content)

    # 点击返回
    @allure.step(title="点击返回")
    def click_back(self):
        self.click(self.back_button)
