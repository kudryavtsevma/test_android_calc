from selenium.common.exceptions import NoSuchElementException
from .locators import MainPageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def send_(self,  how, what, numbers):
        self.driver.find_element(how, what).send_keys(numbers)

    def click_on_operation(self, how, what):
        self.driver.find_element(how, what).click()

    def is_elebent_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def get_text_from_field1(self):
        text = self.driver.find_element(*MainPageLocators.FIRST_NUMBER).text
        return text

    def get_text_from_field2(self):
        text = self.driver.find_element(*MainPageLocators.SECOND_NUMBER).text
        return text

    def field_selection_1(self):
        self.driver.find_element(*MainPageLocators.FIRST_NUMBER).click()

    def field_selection_2(self):
        self.driver.find_element(*MainPageLocators.SECOND_NUMBER).click()