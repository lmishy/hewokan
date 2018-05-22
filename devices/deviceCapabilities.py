#coding:utf-8
from appium import webdriver


def driver_app(platformVersion='5.0.2', deviceName='ac017119'):
    desire_caps = {}
    desire_caps['platformName'] = "Android"
    desire_caps['platformVersion'] = platformVersion
    desire_caps['deviceName'] = deviceName
    #desire_caps['udid'] = udid
    desire_caps['appPackage'] = 'com.chinamobile.cloudapp'
    desire_caps['appActivity'] = 'cn.anyradio.openscreen.StartActivity'
    desire_caps['unicodeKeyboard'] = "True"  # 使得支持Unicode字符
    desire_caps['resetKeyboard'] = "True"
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
    return driver


if __name__ == "__main__":
    driver = driver_app(platformVersion="5.0.2")