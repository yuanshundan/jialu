from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from web_pages.base_page import BasePage


class IndexPage(BasePage):
    """首页类"""
    user_locator = (By.XPATH, '//a[contains(text(),"@139.com")]')

    def get_user_info(self):
        """获取首页的用户名信息"""
        user_ele = self.wait_presence_element(self.user_locator)
        return user_ele
