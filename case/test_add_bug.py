import time
import unittest

from pages.add_bug_page import ZenTaoBug
from selenium import webdriver


class Test_Add_Bug(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver= webdriver.Firefox()
        cls.bug = ZenTaoBug(cls.driver)
        cls.bug.login()
    def test_add_bug(self):
        timestr = time.strftime("%Y_%m_%d_%H_%M_%S")
        title = "测试提交bug" + timestr
        self.bug.add_bug(title)
        result = self.bug.is_add_bug_sucess(title)
        print(result)
        self.assertTrue(result)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__=="__main__":
    unittest.main()