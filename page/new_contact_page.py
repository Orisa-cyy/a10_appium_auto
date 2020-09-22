import allure

from a10_appium_auto.base.base_action import BaseAction

from selenium.webdriver.common.by import By


class NewContactPage(BaseAction):
    local_save_button = By.XPATH, "//*[@text='本地保存']"
    name_edit_button = By.XPATH, "//*[@text='姓名']"
    phone_edit_button = By.XPATH, "//*[@text='电话']"
    save_button = By.ID, "com.android.contacts:id/menu_save"

    # 点击 本地保存
    @allure.step(title="点击本地保存")
    def click_local_save(self):
        self.click(self.local_save_button)

    # 输入姓名
    @allure.step(title="输入姓名")
    def input_name(self, content):
        allure.attach("姓名：", content, allure.attach_type.TEXT)
        self.input(self.name_edit_button, content)
        allure.attach("截图：", self.driver.get_screenshot_as_png(), allure.attach_type.PNG)

    # 输入电话
    @allure.step(title="输入电话")
    def input_phone(self, content):
        self.input(self.phone_edit_button, content)

    # 点击保存
    @allure.step(title="点击保存")
    def click_save(self):
        self.click(self.save_button)
