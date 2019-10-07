from selenium.webdriver.common.by import By
from web_pages.base_page import BasePage


class LoginPage(BasePage):
    """登录页类"""
    username_locator = (By.ID, 'txtUser')
    pwd_locator = (By.ID, 'txtPass')
    flash_locator = (By.XPATH, '//*[@class="form-error-info"]')

    def login(self, username, pwd):
        """登录"""
        user_ele = self.get_user_info()
        pwd_ele = self.get_pwd_info()
        user_ele.send_keys(username)
        pwd_ele.send_keys(pwd)
        user_ele.submit()
        return self.driver

    def get_flash_info(self):
        """获取错误信息"""
        flash_ele = self.wait_presence_element(self.flash_locator)
        return flash_ele

    def get_user_info(self):
        """定位用户名输入框"""
        user_ele = self.wait_presence_element(self.username_locator)
        return user_ele

    def get_pwd_info(self):
        """定位密码输入框"""
        pwd_ele = self.wait_presence_element(self.pwd_locator)
        return pwd_ele

    def clear_user(self):
        """清除用户名输入"""
        return self.get_user_info().clear()

    def clear_pwd(self):
        """清除密码输入"""
        return self.get_pwd_info().clear()

    def clear_user_pwd_info(self):
        """清除用户名和密码输入框"""
        self.clear_user()
        self.clear_pwd()