from selenium import webdriver


def ass_1():
    drv_f = webdriver.Firefox()
    drv_c = webdriver.Chrome()
    drv_f.get("http://ynet.co.il")
    drv_c.get("http://walla.co.il")


#ass_1()
def ass_2():
    drv_c = webdriver.Chrome()
    drv_c.get("http://ynet.co.il")
    title = drv_c.title
    drv_c.refresh()
    if drv_c.title == title:
        print(title)
#ass_2()

def ass_3():
    print("same location")

def ass_4():
    drv_c = webdriver.Chrome()
    drv_c.get("https://translate.google.com/?sl=iw&tl=en&op=translate")
    drv_c.find_element_by_xpath("/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz["
                                "1]/span/span/div/textarea").send_keys("גנן")

#ass_4()