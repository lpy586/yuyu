from selenium import webdriver
import time
import unittest
class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
    def setUp(self):

        self.driver.get("http://chandao.inetposa.com/zentao/user-login-L3plbnRhby8=.html")
        time.sleep(3)
    def tearDown(self):
        self.is_alert_exist()
        self.driver.delete_all_cookies()     #清空cookies
        self.driver.refresh()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def get_login_username(self):
        try:
            t = self.driver.find_element_by_xpath(".//*[@id='userNav']/li/a/span[1]").text
            print(t)
            return t
        except:
            return ""
    def is_alert_exist(self):
        '''判断alert是不是在'''
        time.sleep(4)
        try:
            alert=self.driver.switch_to_alert()
            text=alert.text
            alert.accept()
            return text
        except:
            return ""
    def login(self,user,psw):
        self.driver.find_element_by_id("account").send_keys(user)
        self.driver.find_element_by_name("password").send_keys(psw)
        self.driver.find_element_by_id("submit").click()

    def test01(self):
        '''用例描述：登录成功的用例'''
        self.login("liuquanyue","liuquanyue@2019")
        #t=driver.find_element_by_css_selector(".user-name").text
        time.sleep(4)
        t=self.get_login_username()
        print("获取登录的结果：%s"%t)

        # if t=="刘权乐":
        #     print("登录成功")
        # else:
        #     print("登录失败")
        self.assertTrue(t=="刘权乐")

    def test02(self):
       '''用例描述，登录失败的用例'''
       self.login("liuquanyue123","123456")
       self.driver.find_element_by_id("account").send_keys("liuquanyue222")
       self.driver.find_element_by_name("password").send_keys("liuquanyue@2019eye")
       self.driver.find_element_by_id("submit").click()
       # t=driver.find_element_by_css_selector(".user-name").text
       time.sleep(4)
       t = self.get_login_username()
       print("登录失败，获取的结果为：%s" % t)
       self.assertTrue(1 == 2)  #断言失败加截图
       #self.assertTrue(t == "")



#if __name__=="__main__":
 #   unittest.main()
