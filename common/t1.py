from selenium import webdriver
import time
driver=webdriver.Firefox()
driver.get("http://sh.ganji.com/")
time.sleep(4)
#滚动底部
# js="window.scrollTo(0,document.body.scrollHeight)"
# driver.execute_script(js)
# time.sleep(4)
#回到顶部
# js="window.scrollTo(0,0)"
# driver.execute_script(js)
#滚动到元素
ele=driver.find_element_by_link_text("新车")
driver.execute_script("arguments[0].scrollIntoView()",ele)