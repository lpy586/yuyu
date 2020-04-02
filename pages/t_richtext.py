from selenium import webdriver
from pages.login_page import LoginPage
import time
driver=webdriver.Firefox()
a=LoginPage(driver)
a.login()
driver.get("http://127.0.0.1/zentao/bug-create-1-0-moduleID=0.html")
time.sleep(4)
body="hello world!"
js='document.getElementsByClassName("ke-edit-iframe")[0].contentWindow.document.body.innerHTML="%s"'%body
driver.execute_script(js)