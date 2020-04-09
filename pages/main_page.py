from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def input_to_first_number(self, number1):
        self.send_(*MainPageLocators.FIRST_NUMBER, number1)

    def input_to_second_number(self, number2):
        self.send_(*MainPageLocators.SECOND_NUMBER, number2)

    def press_the_plus_button(self):
        self.click_on_operation(*MainPageLocators.SUM_BUTTON)

    def press_the_minus_button(self):
        self.click_on_operation(*MainPageLocators.DIFFERENSE_BUTTON)

    def press_the_div_button(self):
        self.click_on_operation(*MainPageLocators.DIV_BUTTON)

    def press_the_mult_button(self):
        self.click_on_operation(*MainPageLocators.MULTIPLICATION_BUTTON)

    def press_the_reset_button(self):
        self.click_on_operation(*MainPageLocators.RESET_BUTTON)

    def get_result(self):
        result_lst = self.get_text_from_element(*MainPageLocators.RESULT).split(' = ')
        result = float(result_lst[1].replace(',', '.'))
        return result

    def get_first_input(self):
        text = self.get_text_from_element(*MainPageLocators.FIRST_NUMBER)
        return text

    def get_second_input(self):
        text = self.get_text_from_element(*MainPageLocators.SECOND_NUMBER)
        return text










