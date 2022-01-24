from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
options = ChromeOptions()
# options.setPageLoadStrategy(PageLoadStrategy.normal)
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time
class LoginPage(object):
    user_input = (By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[1]/form/div[1]/div/div/input')
    pwd_input = (By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[1]/form/div[2]/div/div/input')
    login_btn = (By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[1]/form/div[3]/div/button')


    def __init__(self, driver, url='https://pre.adsdesk.cn'):
        #self.options.page_load_strategy = 'normal'
        self.driver = driver
        self.driver.get(url)
        # self.driver.fullscreen_window() 全屏后可能会退出
        self.driver.maximize_window()
    # def login(self, username, password):
    def login(self):
        """
        :param username:
        :param password:
        :return:
        """
        # user_input = (By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[1]/form/div[1]/div/div/input')
        # pwd_input = '//*[@id="app"]/div/div[2]/div/div[2]/div[1]/form/div[2]/div/div/input'
        # login_btn = '//*[@id="app"]/div/div[2]/div/div[2]/div[1]/form/div[3]/div/button'
        try:
            self.driver.find_element(*self.user_input).send_keys('zhangmeng@kuaishou.com')
            self.driver.find_element_by_xpath(*self.pwd_input).send_keys('111111')
            self.driver.find_element_by_xpath(*self.login_btn).click()
        except NoSuchElementException as error:
            print(error)
        except Exception as e:
            print(e)
        finally:
            time.sleep(3)
            self.driver.get_screenshot_as_file('./login1.png')





    def close_driver(self):
        self.driver.close()


log = LoginPage()
log.login()
log.close_driver()
