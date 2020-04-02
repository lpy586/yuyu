#coding:utf-8
from common.base import Base
from selenium import webdriver
driver=webdriver.Firefox()
driver.get("http://127.0.0.1:81/zentao/user-login.html")

class ZenTaoBug():
    #定位登录
    loc1 = ("id", "account")
    loc2 = ("name", "password")
    loc3 = ("id", "submit")

    #添加bug
    loc_test=("link text""测试")
    loc_bug=("link text","Bug")
    loc_addbug=("xpath",".//*[@id='createActionMenu']/a")
    loc_truck=("xpath",".// *[ @ id = 'openedBuild_chosen'] / ul")
    loc_truck_add=("xpath",".// *[ @ id = 'openedBuild_chosen'] / div / ul / li")
    loc_input_title=("id","title")
    loc_avse=("css select","#submit")

    #需要先切换frame
    loc_input_body=("class name",".article-content")
    def __init__(self):
        self.driver=driver
        self.zentao=Base(self.driver)
    def login(self,user="admin",psw="123456"):
        self.zentao.sendkeys(self.loca1,user)
        self.zentao.sendkeys(self.loca2, psw)
        self.zentao.click(self.loca3)



