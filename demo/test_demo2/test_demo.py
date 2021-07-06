# _*_encoding:'utf-8' _*_
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class TestAfter:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://testerhome.com')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_scan(self):
        self.driver.find_element(By.XPATH, '//*[@id="main"]/div/div[1]/div[2]/div[1]/div/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="main"]/div/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a').click()

    def test_nologin(self):
        self.driver.find_element(By.XPATH, '//*[@id="main-nav-menu"]/ul/li[4]/a').click()
        sleep(3)
        self.driver.find_element(By.TAG_NAME, 'team-name').click()
        sleep(6)
        self.driver.find_element(By.CSS_SELECTOR, '[title="第十期_Selenium 第二周_20190801"]').click()
        sleep(5)
        assert "访问被拒绝，你可能没有权限或未登录。" in self.driver.page_source

    def test_errorlogin(self):
        self.driver.find_element(By.XPATH, '//*[@id="main-page"]/div[1]/nav/div/ul[1]/li[2]/a').click()
        sleep(3)
        self.driver.find_element_by_id('user_login').send_keys('zhanglu')
        sleep(3)
        self.driver.find_element_by_name('user[password]').send_keys('123456')
        self.driver.find_element_by_name('connit').click()
        sleep(4)
        assert '账号或密码错误' in self.driver.page_source

    def test_girl(self):
        search = self.driver.find_element_by_name('q')
        search.send_keys('测试媛')
        search.send_keys(Keys.ENTER)
        sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[4]/div[1]/a').click()
        sleep(3)
        assert '测试媛' in self.driver.page_source