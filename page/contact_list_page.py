import allure

from a10_appium_auto.base.base_action import BaseAction

from selenium.webdriver.common.by import By


class ContactListPage(BaseAction):
    add_contact_button = By.ID, "com.android.contacts:id/floating_action_button"

    # 点击 添加联系人
    @allure.step(title="添加联系人")
    def click_add_contact(self):
        self.click(self.add_contact_button)
