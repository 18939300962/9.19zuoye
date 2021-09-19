from xue_001.lianxi004.test_case import test_case
import unittest,HTMLTestRunner_PY3
# 测试套件
suite = unittest.TestSuite()
suite.addTest(test_case("test_case01"))
suite.addTest(test_case("test_case02"))
# 测试执行
zhixing = unittest.TextTestRunner()
zhixing.run(suite)
# 测试报告+执行
# baogao = HTMLTestRunner_PY3.HTMLTestRunner(open("./1.html","wb"),
#                                            title="我的报告",
#                                            description="执行了苏宁易购两条用例")
# baogao.run(suite)