from appium import webdriver


def init_driver_contact():
    desired_caps = dict()
    # 手机参数
    desired_caps['platformName'] = 'android'
    desired_caps['platformVersion'] = '7.1.2'
    desired_caps['deviceName'] = '192.168.56.101:5555'
    # 应用参数
    desired_caps['appPackage'] = 'com.android.contacts'
    desired_caps['appActivity'] = '.activities.PeopleActivity'
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True

    # 获取driver
    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
