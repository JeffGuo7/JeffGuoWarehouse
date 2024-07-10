from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

import time

# 打开支付宝页面
driver = webdriver.Chrome()
driver.get('https://www.alipay.com/')

# 切换到支付页面的iframe中
iframe = driver.find_element_by_id('J_tLoginIframe')
driver.switch_to.frame(iframe)

# 点击扫码支付
sao_ma = driver.find_element_by_class_name('log-btn')
ActionChains(driver).move_to_element(sao_ma).click().perform()

# 输入支付金额
money_input = driver.find_element_by_id('J-input-money')
money_input.send_keys('1')

# 输入支付密码
pwd_input = driver.find_element_by_id('payPassword_rsainput')
pwd_input.send_keys('123456')

# 点击确定支付
pay_btn = driver.find_element_by_id('J_authSubmit')
ActionChains(driver).move_to_element(pay_btn).click().perform()


# 等待二维码扫描完成
time.sleep(5)

# 点击确认支付按钮
confirm_pay = driver.find_element_by_id('J_authSubmit')
ActionChains(driver).move_to_element(confirm_pay).click().perform()

# 等待支付结果页面加载完成
time.sleep(3)

# 关闭浏览器
driver.quit()
