from a10_appium_auto.page.contact_list_page import ContactListPage
from a10_appium_auto.page.mobile_network_page import MobileNetworkPage
from a10_appium_auto.page.more_page import MorePage
from a10_appium_auto.page.new_contact_page import NewContactPage
from a10_appium_auto.page.saved_contact_page import SavedContactPage
from a10_appium_auto.page.search_page import SearchPage
from a10_appium_auto.page.setting_page import SettingPage


# page统一入口
class Page:
    def __init__(self, driver):
        self.driver = driver

    @property
    def more(self):
        return MorePage(self.driver)

    @property
    def search(self):
        return SearchPage(self.driver)

    @property
    def setting(self):
        return SettingPage(self.driver)

    @property
    def mobile_network(self):
        return MobileNetworkPage(self.driver)

    @property
    def contact_list(self):
        return ContactListPage(self.driver)

    @property
    def new_contact(self):
        return NewContactPage(self.driver)

    @property
    def saved_contact(self):
        return SavedContactPage(self.driver)
