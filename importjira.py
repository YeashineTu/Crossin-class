from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import xlrd

##指定打开的浏览器
browser = webdriver.Firefox()

##登入系统  输入用户名密码
browser.get('https://hs-cas.hundsun.com/cas/login?service=http%3A%2F%2Fse.hundsun.com%2Fdm%2Fsecure%2FDashboard.jspa')
browser.find_element_by_id('username').clear()
browser.find_element_by_id('password').clear()
browser.find_element_by_id('username').send_keys('tuyx')
browser.find_element_by_id('password').send_keys('tyx0516@')
browser.find_element_by_name('submit').click()
time.sleep(10)  ##跳转了页面，等待页面加载完全以确保下面的元素可以成功获取


#打开工作表
try:
	data = xlrd.open_workbook('bugreport.xls')
except:
	print("open filed")
#获取Excel的sheet页
sheet = data.sheet_by_name('缺陷记录')
row = sheet.nrows
col = sheet.ncols
print('row:%d,col:%d'%(row,col))
project = '大宗云现货交易系统'
##开始循环
for i in range(1,row):
	summary = sheet.row_values(i)[1]    #概要 描述
	priority = sheet.row_values(i)[2]   #严重度
	origin = sheet.row_values(i)[3]   #缺陷来源
	origin_1 = sheet.row_values(i)[4]   #缺陷来源
	module = sheet.row_values(i)[5]   #模块
	is_unit = sheet.row_values(i)[6]   #是否应单元测试发现
	developer = sheet.row_values(i)[7]   #开发者
	des_stage = sheet.row_values(i)[8]   #缺陷发现阶段
	category = sheet.row_values(i)[9]   #类别
	issue_type = sheet.row_values(i)[10]   #缺陷类型
	level = sheet.row_values(i)[11]        #优先级
	method = sheet.row_values(i)[12]       #测试方法
	print(sheet.row_values(i))    ##打印读取的信息
	##点击创建问题
	browser.find_element_by_id('create_link').click()
	time.sleep(5)  ##跳转了页面，等待页面加载完全以确保下面的元素可以成功获取



	##选择项目名称及缺陷类型
#	browser.find_element_by_id('project').send_keys(project)  有时候获取的数据不对
#	browser.find_element_by_xpath(".//*[@id='issuetype']").send_keys(issue_type)  有时候获取的数据不对
#   browser.find_element_by_id('project').find_element_by_xpath("//option[@value='2017100135']").click() 有时候获取的数据不对
	Select(browser.find_element_by_id('project')).select_by_value('2017100135')
	time.sleep(5)
	browser.find_element_by_name('下一步>>').click()
	time.sleep(5)     ##下一步之后，需要等页面加载完成，不然会找不到下面的元素

	##BUG正文内容
	#概要
	browser.find_element_by_xpath(".//*[@id='summary']").clear()
	browser.find_element_by_xpath(".//*[@id='summary']").send_keys(summary)
	#严重度
	browser.find_element_by_xpath(".//*[@id='priority']").send_keys(priority)
	#优先级
	browser.find_element_by_xpath(".//*[@id='customfield_10300']").send_keys(level)
	#缺陷来源
	browser.find_element_by_xpath(".//*[@id='customfield_10072']").send_keys(origin)
	browser.find_element_by_xpath(".//*[@id='customfield_10072:1']").send_keys(origin_1)
	#模块
	browser.find_element_by_xpath(".//*[@id='components']").send_keys(module)
	#是否应单元测试发现
	browser.find_element_by_xpath(".//*[@id='customfield_10160']").send_keys(is_unit)
	#开发者
	browser.find_element_by_xpath(".//*[@id='assignee']").send_keys(developer)
	#描述
	browser.find_element_by_xpath(".//*[@id='description']").clear()
	browser.find_element_by_xpath(".//*[@id='description']").send_keys(summary)
	# 修改单号  写死0
	browser.find_element_by_xpath(".//*[@id='customfield_10110']").send_keys('0')
	# 缺陷发现阶段
	browser.find_element_by_xpath(".//*[@id='customfield_10290']").send_keys(des_stage)
	#类别
	browser.find_element_by_xpath(".//*[@id='customfield_10000']").send_keys(category)
	#测试方法
	browser.find_element_by_xpath(".//*[@id='customfield_10510']").send_keys(method)

	#提交
	browser.find_element_by_xpath(".//*[@id='创建']").click()
	#提交完后等待
	time.sleep(5)




