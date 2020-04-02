from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

class Base():
    def __init__(self,driver:webdriver.Firefox):
        self.driver=driver
        self.timeout=10
        self.t=0.5
    def findElementNew(self,locator):
        ele=WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator))
        return ele
    def findElement(self,loctor):
        #ele1=WebDriverWait(driver,timeout,t).until(lambda x:x.find_element(loctor[0],loctor[1]))
        ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*loctor))
        return ele
    def findElements(self,loctor):
        if not isinstance(loctor,tuple):
            print("loctor参数类型错误，必须传元祖类型：")
        else:
            print("正在定位元素信息：定位方式->%s,value值->%s"%(loctor[0],loctor[1]))
            eles = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_elements(*loctor))
            return eles
    def sendkeys(self,locator,text):
        ele=self.findElement(locator)
        ele.send_keys(text)
    def click(self,locator):
        ele=self.findElement(locator)
        ele.click()
    def clear(self,locator):
        ele = self.findElement(locator)
        ele.clear()
    def isSelected(self,locator):
        ele=self.findElement(locator)
        r=ele.is_selected()
        return r
    def isElementExist(self ,locator):
        try:
            self.findElement(locator)
            return True
        except:
            return  False
    def isElementExist2(self,locator):
        eles=self.findElements(locator)
        n =len(eles)
        if n==0:
            return False
        elif n==1:
            return True
        else:
            print("定位到元素的个数：%s"%n)
            return True
    def is_title(self,_title):
        try:
          result=WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(_title))
          return result
        except:
            return False
    def is_title_contains(self,_title):
        try:
            result=WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(_title))
            return result
        except:
            return False
    def is_text_in_element(self,locator,_text):
        try:
            result=WebDriverWait(self.driver,self.timeout,self.t).until(EC.text_to_be_present_in_element(locator,_text))
            return result
        except:
            return False
    def is_value_in_element(self,locator,_value):
        try:
            result=WebDriverWait(self.driver,self.timeout,self.t).until(EC.text_to_be_present_in_element(locator,_value))
            return result
        except:
            return False
    def is_alert(self):
        try:
         result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.alert_is_present())
         return result
        except:
            return False
    def get_title(self):
        return self.driver.title
    def get_text(self,locator):
        try:
            t=self.findElement(locator).text
            return t
        except:
            print("获取text失败，返回‘’")
            return ""
    def move_to_element(self,loctor):
        ele=self.findElement(loctor)
        ActionChains(driver).move_to_element(ele).perform()
    def select_by_index(self,loctor,index=0):
        element=self.findElement(loctor)
        Select(element).select_by_index(index)
    def select_by_value(self,loctor,value):
        element=self.findElement(loctor)
        Select(element).select_by_value(value)
    def select_by_text(self,loctor,text):
        element=self.findElement(loctor)
        Select(element).select_by_visible_text(text)
    def js_focus_element(self,loctor):
        ''' 聚焦元素'''
        target=self.findElement(loctor)
        self.driver.execute_script("arguments[0].scrollIntoView()",target)
    def is_scroll_top(self):
        ''' 滚动到顶部'''
        js="window.scrollTo(0,0)"
        self.driver.execute_script(js)
    def is_scroll_end(self):
        ''' 滚动到底部'''
        js="window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)
if __name__=="__main__":
    driver=webdriver.Firefox()
    driver.get("http://chandao.inetposa.com/zentao/user-login-L3plbnRhby8=.html")
    zentao=Base(driver)
    # loc1=(By.ID,"account")
    # loc2 = (By.NAME, "password")
    # loc3 = (By.ID, "submit")
    loc1=("id","account")
    loc2=("css selector","[name='password']")
    loc3=("xpath","//*[@id='submit']")
    zentao.sendkeys(loc1,"liuquanyue")
    zentao.sendkeys(loc2,"liuquanyue@2019")
    zentao.click(loc3)
    zentao.move_to_element()