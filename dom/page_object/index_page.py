# _*_encoding:'utf-8' _*_

'''
    index_page页面对象：实现首页中关于商品搜索的流程
'''

from dom.base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver

class IndexPage(BasePage):
    #核心元素
    url = 'http://39.98.138.157/shopxo/index.php'

    search_input = (By.NAME, 'wd')
    serch_button = (By.ID, 'ai-topsearch')



    #核心业务流
    def serch(self, txt):
        self.visit()
        self.input_(self.search_input, txt)
        self.click(self.serch_button)

# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     txt = '手机'
#     ip = IndexPage(driver)
#     ip.serch(txt)