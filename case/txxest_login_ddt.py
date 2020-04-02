from selenium import webdriver
import unittest
from pages.login_page import LoginPage,login_url
import ddt
from common.read_excel import ExcelUtil
import os
'''
1.输入admin，密码123456，点击登录
2.输入admin，密码为空，点击登录
3.输入admin111，输入123456，点击登录
'''
#
# testdata=[{"user":"admin","psw":"123456","expect":"admin"},
#           {"user":"admin","psw":"","expect":""},
#           {"user":"admin111","psw":"123456","expect":""}
#           ]
propath=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
filepath = os.path.join(propath,"common","datas.xlsx")    #"D:\\python\\study\\web_auto\\common\\datas.xlsx"
print(filepath)
data = ExcelUtil(filepath)
testdata=data.dict_data()
print(testdata)
@ddt.ddt
class LoginPageCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.loginp=LoginPage(cls.driver)
        cls.driver.get(login_url)
    def setUp(self):
        self.loginp.is_alert_exist()
        self.driver.delete_all_cookies()  # 清空cookies
        self.driver.refresh()
        self.driver.get(login_url)
    def login_case(self,user,psw,expect):
        self.loginp.input_user(user)
        self.loginp.input_psw(psw)
        self.loginp.click_login_button()
        #self.loginp.login()
        result = self.loginp.get_login_name()
        print("测试结果：%s"%result)
        self.assertTrue(result == expect)
    # @ddt.data({"user":"admin","psw":"123456","expect":"admin"},
    #     {"user":"admin","psw":"","expect":""},
    #     {"user":"admin111","psw":"123456","expect":""} )
    @ddt.data
    def test_01(self,data):
        ''' 登录'''
        print("----------开始测试：---------")
        print("测试数据:%s"%data)
        self.login_case(data["user"],data["psw"],data["expect"])
        print("----------结束测试：---------")
    # def tearDown(self):
    #     self.loginp.is_alert_exist()
    #     self.driver.delete_all_cookies()  # 清空cookies
    #     self.driver.refresh()
    # def test_02(self):
    #     '''    密码为空 '''
    #     print("----------开始测试：test_02---------")
    #     data2=testdata[1]
    #     print("测试数据%s"%data2)
    #     self.login_case(data2["user"],data2["psw"],data2["expect"])
    #     print("----------结束测试：test_02---------")
    # def test_03(self):
    #     print("----------开始测试：test_03---------")
    #     data3 = testdata[2]
    #     print("测试数据%s" % data3)
    #     self.login_case(data3["user"], data3["psw"], data3["expect"])
    #     print("----------结束测试：test_03---------")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__=="__main__":
     unittest.main()
