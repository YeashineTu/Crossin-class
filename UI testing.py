from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://www.baidu.com')
browser.find_element_by_class_name('s_ipt').send_keys('1')