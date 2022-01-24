from selenium.webdriver.common.by import By

class AdBase(object):
    def __init__(self, driver):
        self.driver = driver
    # 投放账户
        self.account_select = (By.XPATH, '//*[@id="adCreateAiBasicConfig"]/div[2]/div/div/form/div[1]/div/div/div[1]/div/i')
    # 营销链路（营销场景）
        self.marketing_scenario = (By.XPATH, '//*[@id="adCreateAiBasicConfig"]/div[2]/div/div/form/div[2]/div/div/label[2]')
    # 推广目标-应用
        self.promotion_target = (By.XPATH, '//*[@id="adCreateAiBasicConfig"]/div[2]/div/div/form/div[4]/div/div/label[1]')
    # 推广目标-销售线索
        self.sales_lead = (By.XPATH, '//*[@id="adCreateAiBasicConfig"]/div[2]/div/div/form/div[4]/div/div/label[2]')
    # 推广目标-直播
        self.live = (By.XPATH, '//*[@id="adCreateAiBasicConfig"]/div[2]/div/div/form/div[4]/div/div/label[3]')
    # 推广目标-快应用
        self.quick_app = (By.XPATH, '//*[@id="adCreateAiBasicConfig"]/div[2]/div/div/form/div[4]/div/div/label[4]')
    # 推广目标-商品
        self.commodity = (By.XPATH, '//*[@id="adCreateAiBasicConfig"]/div[2]/div/div/form/div[4]/div/div/label[5]')
    # 推广目标-应用
        self.e_commerce = (By.XPATH, '//*[@id="adCreateAiBasicConfig"]/div[2]/div/div/form/div[4]/div/div/label[6]')
    # 标准投放-投放类别
        self.delivery_category_standard = (By.XPATH, '//*[@id="adCreateAiBasicConfig"]/div[2]/div/div/form/div[5]/div/div/label[1]')
    # 单品投放-投放类别
        self.delivery_category_single = (By.XPATH, '//*[@id="adCreateAiBasicConfig"]/div[2]/div/div/form/div[5]/div/div/label[2]')
    # Android推广平台
        self.marketing_platform_android = (By.XPATH, '//*[@id="adCreateAiBasicConfig"]/div[2]/div/div/form/div[6]/div/div/label[12')
    # IOS推广平台（Android(默认)）
        self.marketing_platform_ios = (By.XPATH, '//*[@id="adCreateAiBasicConfig"]/div[2]/div/div/form/div[6]/div/div/label[1]')
    # 选择应用窗口
        self.select_application = (By.XPATH, '//*[@id="adCreateAiBasicConfig"]/div[2]/div/div/form/div[7]/div/button/span')
    # 选择抖音号(直播间)
        self.select_douyin = (By.XPATH, '//*[@id="adCreateAiBasicConfig"]/div[2]/div/div/form/div[6]/div/button/span')
    # 选择应用页面
        # 搜索应用
        self.search_app = (By.XPATH, '/html/body/div[136]/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/input')
        # 选择应用
        self.select_first_app = (By.XPATH, '/html/body/div[136]/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[1]')
        # 确定按钮
        self.sure_button = (By.XPATH, '/html/body/div[137]/div[2]/div/div/div[3]/div/button[3]')

        # 选择抖音号页面

    def base(self, marketing_link='purpose', target='app'):
        platform = 'Android'
        category = 'standard'
        # 预约或应用推广，可选择平台
        if marketing_link == 'scenario' or target == 'app':
            if platform == 'IOS':
                try:
                    self.driver.find_element(*self.marketing_platform_ios).click()
                except Exception as e:
                    print(e)
            elif platform == 'Android':
                try:
                    self.driver.find_element(*self.marketing_platform_android).click()
                except Exception as e:
                    print(e)
            else:
                print('platform error')

        if category == 'single':
            try:
                self.driver.find_element(*self.delivery_category_single).click()
            except Exception as e:
                print(e)
        elif category == 'standard':
            try:
                self.driver.find_element(*self.delivery_category_standard).click()
            except Exception as e:
                print(e)
        else:
            print('category error')

# 通过搜索，选择第一个app
    def select_first_app(self, searchkey=240687):
        # 搜索应用
        try:
            self.driver.find_element(*self.search_app).sendkeys(searchkey)
            self.driver.find_element(*self.select_first_app).click()
            self.driver.find_element(*self.sure_button).click()
        except Exception as e:
            print(e)






