#coding:utf-8

import unittest
from devices import deviceCapabilities
from appium import webdriver
from time import sleep
from action import move


class test_login(unittest.TestSuite):
    def setUp(self):
        self.driver = deviceCapabilities.driver_app()
        print("\n---------------------------执行 setUp 取到 .app 包---------------------------")

    def tearDown(self):
        self.driver.quit()

    def test_first(self):
        print("here is first")
        sleep(10)
        move.swipLeft(1000)
        sleep(3)
        move.swipLeft(1000)
        sleep(3)
        move.swipLeft(1000)
        sleep(3)
        move.swipLeft(1000)
        sleep(3)
        self.driver.find_element_by_id("com.chinamobile.cloudapp:id/btn_into_home").click()
        sleep(3)
        self.driver.find_element_by_id("com.chinamobile.cloudapp:id/root_bottom_home_tab_5").click()
        sleep(3)
        self.driver.find_element_by_id("com.chinamobile.cloudapp:id/layout_setting").click()
        sleep(3)
        self.driver.find_element_by_id("com.chinamobile.cloudapp:id/layout_recomm").click()
        sleep(3)

    def test_login_sccess(self):
        print("hellp")
        self.driver.find_element_by_id("com.chinamobile.cloudapp:id/tv_user_name").click()
        sleep(2)
        self.driver.find_element_by_id("com.chinamobile.cloudapp:id/edittext_phone").send_keys("18428027801")
        sleep(2)
        self.driver.find_element_by_id("com.chinamobile.cloudapp:id/edittext_pwd").send_keys("qqq111")
        sleep(2)
        self.driver.find_element_by_id("com.chinamobile.cloudapp:id/button_login").click()
        sleep(5)



if __name__ == "__main__":
    unittest.main()