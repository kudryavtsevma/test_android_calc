import time

import pytest
from appium import webdriver


desired_caps = {
    'platformName': 'Android',
    'deviceName': 'Android Emulator',
    'automationName': 'UiAutomator2',
}


def pytest_addoption(parser):
    parser.addoption('--android_version', action='store', default='10.0',
                     help="android_version")
    parser.addoption('--apk', action='store', default=None,
                     help="APK")


@pytest.fixture(scope="function", name='driver')
def get_driver_fixture(request):
    package = 'com.vbanthia.androidsampleapp'
    app_activity = 'MainActivity'
    desired_caps['platformVersion'] = request.config.getoption("android_version")
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    driver.start_activity(package, app_activity)
    yield driver
    driver.close_app()
    driver.quit()


@pytest.fixture(scope="session", name='install_application')
def get_install_application_fixture(driver, request):
    app = request.config.getoption("apk")
    desired_caps['platformVersion'] = request.config.getoption("android_version")
    driver.install_app(app)
    time.sleep(10)
