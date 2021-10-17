from selenium import webdriver

from time import sleep
my_driver = webdriver.Chrome(executable_path="C:/Users/razo/Downloads/chromedriver.exe")
my_driver.get("file://C:/Users/razo/PycharmProjects/Devops0909/tip_calc/index.html")
my_driver.find_element_by_id("billamt").send_keys("100")
my_driver.find_element_by_xpath('//*[@id="serviceQual"]/option[4]').click()
my_driver.find_element_by_xpath('//*[@id="musicQual"]/option[3]').click()
my_driver.find_element_by_id("peopleamt").send_keys("5")
my_driver.find_element_by_id("calculate").click()
expected = "7.00"
actual = my_driver.find_element_by_id("tip").text
my_driver.close()
if expected == actual:
    print("all good")

