import allure

from a10_appium_auto.base.base_action import BaseAction

from selenium.webdriver.common.by import By


class SavedContactPage(BaseAction):
    name_title_feature = By.ID, "com.android.contacts:id/large_title"

    # 获取 大标题名称
    @allure.step(title="获取联系人姓名")
    def get_contact_title_text(self):
        return self.find_element(self.name_title_feature).text
