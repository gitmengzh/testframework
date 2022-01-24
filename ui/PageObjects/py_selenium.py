 # 封装Selenium常用方法
class seleniumMethods(object):
    def __init__(self, driver):
        self.driver = driver
# 构造函数

    def getTitle(self):
        # 获取页面标题
        return self.driver.title

    def clearAndInput(self, location, value):
        # 根据xpath定位元素并清除、输入
        element = self.driver.find_element_by_xpath(location)
        element.clear()
        element.send_keys(value)

    def click(self, location):
        # 根据xpath定位元素并点击
        return self.driver.find_element_by_xpath(location).click()

    def getText(self, location):
        # 根据xpath定位元素并获取文本值
        return self.driver.find_element_by_xpath(location).text