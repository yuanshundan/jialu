from selenium.webdriver import Chrome
from web_pages.index_page import IndexPage
from web_pages.login_page import LoginPage


class TestLogin():
    """测试类"""
    def __init__(self):
        self.driver = Chrome()

    def test_2_login_success(self, url, user, pwd):
        """测试登陆成功"""
        self.driver.get(url)
        self.driver.get_window_size()
        # 调用登录页面的函数login（）成定位输入框并填写登录名和密码
        LoginPage(self.driver).login(user, pwd)
        # 定位首页登录成功  调用首页的get_user_info()
        user_ele = IndexPage(self.driver).get_user_info()
        # 断言
        return user_ele.text
