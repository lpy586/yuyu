#coding:utf-8
from common.base import Base
from selenium import webdriver
import time
#driver=webdriver.Firefox()
#driver.get("http://127.0.0.1:81/zentao/user-login.html")
class ZenTaoBugPage(Base):     #继承 #定位登录

    #添加bug
    loc_test=("link text","测试")
    loc_bug=("link text","Bug")
    loc_addbug=("xpath",".//*[@id='createActionMenu']/a")
    loc_truck=("xpath",".// *[ @ id = 'openedBuild_chosen'] / ul")
    loc_truck_add=("xpath",".// *[ @ id = 'openedBuild_chosen'] / div / ul / li")
    loc_input_title=("id","title")
    # 需要先切换frame
    loc_input_body = ("class name", "article-content")
    loc_avse=("css selector","#submit")
    #新增的列表
    loc_new=("xpath",".//*[@id='bugList']/tbody/tr[1]/td[4]/a")
    def add_bug(self,title):
        self.click(self.loc_test)
        self.click(self.loc_bug)
        self.click(self.loc_addbug)
        self.click(self.loc_truck)
        self.click(self.loc_truck_add)
        self.sendkeys(self.loc_input_title,title)
        frame=self.findElement(("class name","ke-edit-iframe"))
        self.driver.switch_to.frame(frame)
        #附文本不能clear
        body='''[测试步骤]
        [结果]
        [期望结果]
        '''
        self.sendkeys(self.loc_input_body,body)
        self.driver.switch_to_default_content()
        self.click(self.loc_avse)
    def is_add_bug_sucess(self,_text):
        return self.is_text_in_element(self.loc_new,_text)
if __name__=="__main__":

     driver=webdriver.Firefox()
     bug = ZenTaoBugPage(driver)
     from pages.login_page import LoginPage
     a=LoginPage(driver)
     a.login()
     timestr = time.strftime("%Y_%m_%d_%H_%M_%S")
     title="测试提交bug"+timestr
     bug.add_bug(title)
     result=bug.is_add_bug_sucess(title)
     print(result)