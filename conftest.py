import time

import pytest
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

desired_caps = {
    'platformName': 'Android',
    'deviceName': 'Android Emulator',
    'automationName': 'UiAutomator2',
}

package = 'com.vbanthia.androidsampleapp'
app_activity = 'MainActivity'


def pytest_addoption(parser):
    parser.addoption('--android_version', action='store', default='10.0',
                     help="android_version")
    parser.addoption('--apk', action='store', default=None,
                     help="APK")


@pytest.fixture(scope="session", autouse=True)
def get_install_application_fixture(request):
    app = request.config.getoption("apk")

    desired_caps['platformVersion'] = request.config.getoption("android_version")
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    driver.install_app(app)
    try:
        driver.start_activity(package, app_activity)
        driver.find_element_by_id('android:id/button1').click()
        driver.close_app()
        driver.quit()
    except NoSuchElementException:
        pass



@pytest.fixture(scope="function", name='driver')
def get_driver_fixture(request):
    desired_caps['platformVersion'] = request.config.getoption("android_version")
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    driver.implicitly_wait(5000)
    driver.start_activity(package, app_activity)
    yield driver
    driver.quit()



