from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import logging # logger
from selenium.webdriver import Chrome


class BasePage:

    def __init__(self, driver: Chrome):
        self.driver = driver

    def wait_visible_element(self, locator, equency=20):
        """定时等待元素出现"""
        try:
            return WebDriverWait(self.driver, equency).until(
                ec.visibility_of_element_located(locator))
        except Exception as e:
            # logging.error('元素定位失败')
            # 截屏
            self.driver.save_screenshot('test.png')

    def wait_presence_element(self, locator,equency=20):
        """等待元素出现"""
        try:
            return  WebDriverWait(self.driver, equency).until(
                ec.presence_of_element_located(locator))
        except Exception as e:
            # logging.error('元素定位失败')
            # 截屏
            self.driver.save_screenshot('test.jpg')

    def wait_clickable_element(self, locator,equency=20):
        """等待元素出现点击"""
        return WebDriverWait(self.driver, equency).until(
            ec.element_to_be_clickable(locator))

    def switch_window(self, fqc=20, name='None'):
        """切换窗口"""
        if not name:
            handles = self.driver.window_handles
            current_handle = self.driver.current_window_handle
            WebDriverWait(self.driver, timeout=fqc).until(ec.new_window_is_opened)
            return self.driver.switch_to.window(handles[-1])
        return self.driver.switch_to.window(name)

    # def switch_iframe(self, iframe):
    #     """切换iframe"""
    #     iframes = self.driver.iframe
    #     for c in iframes:
    #         # 切换到默认界面
    #         if c == iframe:
    #             self.driver.switch_to.iframe(iframe)
    #
    # def switch_alert(self, alert):
    #     """切换，alert"""
    #     alerts = self.driver.alert
    #     for c in alerts:
    #         # 切换到默认界面
    #         if c == alert:
    #             self.driver.switch_to.alert(alert)

    def click(self, locator):
        """点击"""
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(locator))

    def send_keys(self):
        pass