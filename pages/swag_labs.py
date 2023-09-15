from selenium.common.exceptions import NoSuchDriverException
from pages.base_page import BasePage

class SwagLabs(BasePage):

    def exist_icon(self):
        try:
            self.find_element(locator="div.login_logo")
        except NoSuchDriverException:
            return False
        return True
