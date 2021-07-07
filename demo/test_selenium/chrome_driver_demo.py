# _*_encoding:'utf-8' _*_
#同样的流程不一样的代码
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
#创建webdriver对象
wb = WebDriver(executable_path = "chromedriver")
#访问url
wb.execute('get',{'url': 'https://www.baidu.com'})
#定位到输入文本框进行输入
el = wb.execute('findElement',{
    'using': By.XPATH,
    'value': '//input[@id="kw"]'
})['value']
el._execute('sendKeysToElement',{
    'text': '小龙女',
    'value': ''
})
#定位到百度一下按钮,进行点击
# driver.find_element('id', 'su').click()



