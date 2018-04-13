from selenium import webdriver
import time
import xlrd

##指定打开的浏览器
browser = webdriver.Firefox()

##登入系统  输入用户名密码
browser.get('https://hs-cas.hundsun.com/cas/login?service=http%3A%2F%2Fse.hundsun.com%2Fdm%2Fsecure%2FDashboard.jspa')
browser.find_element_by_id('username').clear()
browser.find_element_by_id('password').clear()
browser.find_element_by_id('username').send_keys('tuyx')
browser.find_element_by_id('password').send_keys('tyx@@0516')
browser.find_element_by_name('submit').click()
time.sleep(10)  ##跳转了页面，等待页面加载完全以确保下面的元素可以成功获取

##点击创建问题
browser.find_element_by_id('create_link').click()
time.sleep(5)  ##跳转了页面，等待页面加载完全以确保下面的元素可以成功获取

##选择项目名称及缺陷类型
browser.find_element_by_xpath(".//*[@id='project']").send_keys('大宗云现货交易系统')
browser.find_element_by_xpath(".//*[@id='issuetype']").send_keys('缺陷')
browser.find_element_by_name('下一步>>').click()
time.sleep(5)     ##下一步之后，需要等页面加载完成，不然会找不到下面的元素

##BUG正文内容
#概要
browser.find_element_by_xpath(".//*[@id='summary']").send_keys('测试测试')
#严重度
browser.find_element_by_xpath(".//*[@id='priority']").send_keys('小缺陷')
#缺陷来源
browser.find_element_by_xpath(".//*[@id='customfield_10072']").send_keys('设计活动')
browser.find_element_by_xpath(".//*[@id='customfield_10072:1']").send_keys('设计遗漏项')
#模块
browser.find_element_by_xpath(".//*[@id='components']").send_keys('OTC')
#是否应单元测试发现
browser.find_element_by_xpath(".//*[@id='customfield_10160']").send_keys('是')
#开发者
browser.find_element_by_xpath(".//*[@id='assignee']").send_keys('孙耀辉')
#描述
browser.find_element_by_xpath(".//*[@id='description']").send_keys('描述描述')
# 修改单号
browser.find_element_by_xpath(".//*[@id='customfield_10110']").send_keys('0')
# 缺陷发现阶段
browser.find_element_by_xpath(".//*[@id='customfield_10290']").send_keys('需求评审')
# 类别
browser.find_element_by_xpath(".//*[@id='customfield_10000']").send_keys('D.文  档')
#提交
browser.find_element_by_xpath(".//*[@id='创建']").click()


