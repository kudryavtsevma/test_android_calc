from appium.webdriver.common.mobileby import MobileBy


class MainPageLocators():
    FIRST_NUMBER = (MobileBy.ACCESSIBILITY_ID, 'inputFieldLeft')
    SECOND_NUMBER = (MobileBy.ACCESSIBILITY_ID, 'inputFieldRight')
    SUM_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'additionButton')
    RESULT = (MobileBy.ACCESSIBILITY_ID, 'resultTextView')
    DIV_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'divisionButton')
    DIFFERENSE_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'subtractButton')
    MULTIPLICATION_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'multiplicationButton')
    RESET_BUTTON = (MobileBy.ACCESSIBILITY_ID,'resetButton')

