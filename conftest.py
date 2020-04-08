import pytest
from appium import webdriver


def pytest_addoption(parser):
    parser.addoption('--android_version', action='store', default='10.0',
                     help="android_version")


@pytest.fixture(scope="module", autouse=True)
def driver(request):
    packege = 'com.vbanthia.androidsampleapp'
    app_activity = 'MainActivity'
    android_version = request.config.getoption("android_version")
    desired_caps = {
        'platformName': 'Android',
    'platformVersion': android_version,
    'deviceName': 'Android Emulator',
    'automationName': 'UiAutomator2',
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    driver.start_activity(packege, app_activity)
    yield driver
    driver.quit()


@pytest.fixture(scope="session", autouse=True)
def setup_app():
    app = r'C:\AndroidSDK\app-debug.apk'
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '10.0',
        'deviceName': 'Android Emulator',
        'automationName': 'UiAutomator2',
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    driver.install_app(app)
    driver.quit()
