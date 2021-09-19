import unittest
from xue_001.lianxi004.Fengzpage import Fengzpage
from selenium import webdriver

class test_case(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Firefox()

    def tearDown(self) -> None:
        self.driver.quit()
        # pass
    def test_case01(self):     #登录业务
        po = Fengzpage(self.driver)
        po.syqqdl()
        #断言
        self.assertIn(self.driver.find_element_by_class_name("search-btn.btn-new"),"搜索")
    def test_case02(self):    #商品搜索业务
        po = Fengzpage(self.driver)
        # po.syqqdl()
        po.snjrgwc()
        # 断言
        dy = self.driver.find_element_by_id("addCart").text
        self.assertIn(dy,"加入购物车")

        # self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()
