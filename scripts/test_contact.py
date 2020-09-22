import pytest
import time

from a10_appium_auto.base.base_analyze import analyze_file
from a10_appium_auto.base.base_driver_contact import init_driver_contact
from ..page.page import Page


class TestDisplay:
    def setup(self):
        self.driver = init_driver_contact()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @pytest.mark.parametrize("args", analyze_file("contact_data.yaml", "test_contact"))
    def test_contact(self, args):
        name = args["name"]
        phone = args["phone"]
        self.page.contact_list.click_add_contact()
        self.page.new_contact.click_local_save()
        self.page.new_contact.input_name(name)
        self.page.new_contact.input_phone(phone)
        self.page.new_contact.click_save()

        # 断言 判断输入的姓名和保存过后的姓名是否一致
        assert name == self.page.saved_contact.get_contact_title_text()
