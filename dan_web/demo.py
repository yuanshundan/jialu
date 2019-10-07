import time

from selenium.webdriver.common.by import By

from web_pages.base_page import BasePage

from selenium.webdriver import Chrome

driver = Chrome()
driver.get("https://www.taobao.com/")
time.sleep(3)
ele = BasePage(driver).wait_clickable_element((By.XPATH, '//*[@class="mod" and @data-spm-ab="2"]'))
time.sleep(3)
ele.click()



