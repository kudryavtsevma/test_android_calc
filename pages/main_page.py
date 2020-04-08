from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def plus(self, number1, number2):
        self.send_(*MainPageLocators.FIRST_NUMBER, number1)
        self.send_(*MainPageLocators.SECOND_NUMBER, number2)
        self.click_on_operation(*MainPageLocators.SUM_BUTTON)
        result_lst = self.driver.find_element(*MainPageLocators.RESULT).text.split(' = ')
        x = float(result_lst[1].replace(',', '.'))

        assert x == float(number1) + float(number2), f'Результат сложения {x} посчитан не верно, правильный результат ' \
                                                     f'{float(number1) + float(number2)}'

    def minus(self,number1, number2):
        self.send_(*MainPageLocators.FIRST_NUMBER, number1)
        self.send_(*MainPageLocators.SECOND_NUMBER, number2)
        self.click_on_operation(*MainPageLocators.DIFFERENSE_BUTTON)
        result_lst = self.driver.find_element(*MainPageLocators.RESULT).text.split(' = ')
        x = float(result_lst[1].replace(',', '.'))
        assert x == float(number1) - float(number2), f'Результат вычитания {x} посчитан не верно, правильный результат ' \
                                                     f'{float(number1) - float(number2)}'

    def multiplication(self,number1, number2):
        self.send_(*MainPageLocators.FIRST_NUMBER, number1)
        self.send_(*MainPageLocators.SECOND_NUMBER, number2)
        self.click_on_operation(*MainPageLocators.MULTIPLICATION_BUTTON)
        result_lst = self.driver.find_element(*MainPageLocators.RESULT).text.split(' = ')
        x = float(result_lst[1].replace(',', '.'))
        assert x == float(number1) * float(number2), f'Результат умножения {x} посчитан не верно, правильный результат ' \
                                                     f'{float(number1) * float(number2)}'

    def division(self, number1, number2):
        self.send_(*MainPageLocators.FIRST_NUMBER, number1)
        self.send_(*MainPageLocators.SECOND_NUMBER, number2)
        self.click_on_operation(*MainPageLocators.DIV_BUTTON)
        result_lst = self.driver.find_element(*MainPageLocators.RESULT).text.split(' = ')
        x = float(result_lst[1].replace(',', '.'))
        assert x == float(number1) / float(number2), f'Результат деления {x} посчитан не верно, правильный результат ' \
                                                     f'{float(number1) / float(number2)}'

    def divizion_by_zero(self, number1, number2=0):
        self.send_(*MainPageLocators.FIRST_NUMBER, number1)
        self.send_(*MainPageLocators.SECOND_NUMBER, number2)
        self.click_on_operation(*MainPageLocators.DIV_BUTTON)
        result_lst = self.driver.find_element(*MainPageLocators.RESULT).text.split(' = ')
        assert result_lst[1] == 'Infinity', 'Результат деления на 0 должен быть равен  "Infinity"'

    def digit_response1(self, num1):
        self.send_(*MainPageLocators.FIRST_NUMBER, num1)


    def digit_response2(self, num2):
        self.send_(*MainPageLocators.SECOND_NUMBER, num2)


    def reset_button(self):
        self.click_on_operation(*MainPageLocators.RESET_BUTTON)
        first_number = self.get_text_from_field1()
        second_number = self.get_text_from_field2()
        assert first_number == '', "Поле 1 не сбросилось"
        assert second_number == '', "Поле 1 не сбросилось"

    def data_entry_field_is_empty(self):
        first_number = self.get_text_from_field1()
        second_number = self.get_text_from_field2()
        assert first_number == '', 'Поле для ввода первого числа не пустое'
        assert second_number == '', 'Поле для ввода второго числа не пустое'

    def should_be_all_buttons(self):
        assert self.is_elebent_present(*MainPageLocators.SUM_BUTTON), 'Кнопка сложения не найдена'
        assert self.is_elebent_present(*MainPageLocators.DIV_BUTTON), 'Кнопка деления не найдена'
        assert self.is_elebent_present(*MainPageLocators.DIFFERENSE_BUTTON), 'Кнопка вычитания не найдена'
        assert self.is_elebent_present(*MainPageLocators.MULTIPLICATION_BUTTON), 'Кнопка умножения не найдена'
        assert self.is_elebent_present(*MainPageLocators.RESET_BUTTON), 'Кнопка сброса не найдена'