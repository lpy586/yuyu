import unittest
from common import HTMLTestRunner_cn
#用例的路径
casePath="D:\\python\\study\\web_auto\\case"
rule="test*.py"
discover=unittest.defaultTestLoader.discover(start_dir=casePath,pattern=rule)
print(discover)

reportPath="D:\\python\\study\\web_auto\\report\\"+"result.html"
fp=open(reportPath,"wb")
runner=HTMLTestRunner_cn.HTMLTestRunner(stream=fp,title="报告的title",description="描述报告干什么用")

runner.run(discover)
fp.close()