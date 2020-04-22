# author: liming
# date: 2020/4/7
from selenium import webdriver
import unittest
import HTMLTestRunner
import time


class Test(unittest.TestCase):
    """百度搜索测试"""
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        # self.driver.implicitly_wait(10)

    def test_case1(self):  #百度搜索用例
        """搜索关键字"""
        driver = self.driver
        driver.get("https://www.baidu.com")
        driver.find_element_by_id("kw").send_keys("剑来")
        driver.find_element_by_id("su").click()
        time.sleep(3)
        assert u"剑来" in self.driver.page_source, "页面中不存在要搜索的关键字"

    @classmethod
    def tearDown(cls):
        print("111")


if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    test_suite.addTest(Test("test_case1"))
    filename = "D:/Python/pycharm/自动化测试/Logs/test3.html"
    xx = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=xx, title='百度测试报告', description='用例执行情况:')
    runner.run(test_suite)
    xx.close()
    print("测试完成")