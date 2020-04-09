import pytest
from .pages.locators import MainPageLocators
from .pages.main_page import MainPage


def test_should_be_all_buttons(driver):
    page = MainPage(driver)
    assert page.is_elebent_present(*MainPageLocators.SUM_BUTTON), 'Кнопка сложения не найдена'
    assert page.is_elebent_present(*MainPageLocators.DIV_BUTTON), 'Кнопка деления не найдена'
    assert page.is_elebent_present(*MainPageLocators.DIFFERENSE_BUTTON), 'Кнопка вычитания не найдена'
    assert page.is_elebent_present(*MainPageLocators.MULTIPLICATION_BUTTON), 'Кнопка умножения не найдена'
    assert page.is_elebent_present(*MainPageLocators.RESET_BUTTON), 'Кнопка сброса не найдена'


def test_check_that_the_first_field_are_empty_after_run_app(driver):
    """Проверка, что поля пустые """
    page = MainPage(driver)
    assert page.get_first_input() == '', 'Поле для ввода первого числа не пустое'


def test_check_that_the_second_field_are_empty_after_run_app(driver):
    """Проверка, что поля пустые """
    page = MainPage(driver)
    assert page.get_second_input() == '', 'Поле для ввода первого числа не пустое'


def test_check_that_the_reset_button(driver):
    page = MainPage(driver)
    page.input_to_first_number(12)
    page.input_to_second_number(12)
    page.press_the_reset_button()
    assert page.get_first_input() == '', 'Поле для ввода первого числа не сбросилось'
    assert page.get_second_input() == '', 'Поле для ввода первого числа не сбросилось'


@pytest.mark.parametrize('num1', ['%', 'gg'])
def test_input_is_not_int_or_float_1(driver, num1):
    """Вводим буквы и символы в поле 1"""
    page = MainPage(driver)
    page.input_to_first_number(num1)
    assert page.get_first_input() == '', 'В Поле 1 ввелись буквы или символы'


@pytest.mark.parametrize('num2', ['gg', '%'])
def test_input_is_not_int_or_float_2(driver, num2):
    """Вводим буквы и символы в поле 2"""
    page = MainPage(driver)
    page.input_to_second_number(num2)
    assert page.get_second_input() == '', 'В Поле 2 ввелись буквы или символы'


@pytest.mark.parametrize('num1', [9, 0])
@pytest.mark.parametrize('num2', [0, 9])
def test_dif_0_9(driver,  num2, num1):
    """Проверка функции вычитания с ислами 0 и 9"""
    page = MainPage(driver)
    page.input_to_first_number(num1)
    page.input_to_second_number(num2)
    page.press_the_minus_button()
    assert page.get_result() == float(num1) - float(num2), 'Результат вычитания  посчитан не верно'


@pytest.mark.parametrize('num1', [-9, 1])
@pytest.mark.parametrize('num2', [1, -9])
def test_dif_negative(driver,  num2, num1):
    """Проверка функции вычитания с отрицательными"""
    page = MainPage(driver)
    page.input_to_first_number(num1)
    page.input_to_second_number(num2)
    page.press_the_minus_button()
    assert page.get_result() == float(num1) - float(num2), 'Результат вычитания  посчитан не верно'


@pytest.mark.parametrize('num1', [6, 2])
@pytest.mark.parametrize('num2', [8, 3])
def test_dif_overflow_and_positive(driver,  num2, num1):
    """Проверка функции вычитания с переполнением десятка и без"""
    page = MainPage(driver)
    page.input_to_first_number(num1)
    page.input_to_second_number(num2)
    page.press_the_minus_button()
    assert page.get_result() == float(num1) - float(num2), 'Результат вычитания  посчитан не верно'


@pytest.mark.parametrize('num1', [0, 11])
@pytest.mark.parametrize('num2', [9999999, 9999999999])
def test_dif_many_numbers(driver,  num2, num1):
    """Проверка функции вычитания с большими числами"""
    page = MainPage(driver)
    page.input_to_first_number(num1)
    page.input_to_second_number(num2)
    page.press_the_minus_button()
    assert page.get_result() == float(num1) - float(num2), 'Результат вычитания  посчитан не верно'


@pytest.mark.parametrize('num1', [str(1.1), str(9.9), str(99.15), str(99.99), str(99.150), str(99.999)])
def test_dif_float(driver, num1, num2=1):
    """Проверка функции вычитания с дробными числами"""
    page = MainPage(driver)
    page.input_to_first_number(num1)
    page.input_to_second_number(num2)
    page.press_the_minus_button()
    assert page.get_result() == float(num1) - float(num2), 'Результат вычитания  посчитан не верно'


@pytest.mark.parametrize('num1', [9, 0])
@pytest.mark.parametrize('num2', [0, 9])
def test_sum_0_9(driver, num1, num2):
    """Проверка функции сложения с числами 0 и 9"""
    page = MainPage(driver)
    page.input_to_first_number(num1)
    page.input_to_second_number(num2)
    page.press_the_plus_button()
    assert page.get_result() == float(num1) + float(num2), 'Результат сложения  посчитан не верно'


@pytest.mark.parametrize('num1', [-9, 1])
@pytest.mark.parametrize('num2', [1, -9])
def test_sum_negative(driver,  num2, num1):
    """Проверка функции сложения с отрицательными"""
    page = MainPage(driver)
    page.input_to_first_number(num1)
    page.input_to_second_number(num2)
    page.press_the_plus_button()
    assert page.get_result() == float(num1) + float(num2), 'Результат сложения  посчитан не верно'


@pytest.mark.parametrize('num1', [6, 2])
@pytest.mark.parametrize('num2', [8, 3])
def test_sum_overflow_and_positive(driver, num1, num2):
    """Проверка функции сложения с переполнением десятка и без"""
    page = MainPage(driver)
    page.input_to_first_number(num1)
    page.input_to_second_number(num2)
    page.press_the_plus_button()
    assert page.get_result() == float(num1) + float(num2), 'Результат сложения  посчитан не верно'


@pytest.mark.parametrize('num1', [9999999999, 11])
@pytest.mark.parametrize('num2', [11, 9999999999])
def test_sum_many_numbers(driver,  num2, num1):
    """Проверка функции сложения с большими числами"""
    page = MainPage(driver)
    page.input_to_first_number(num1)
    page.input_to_second_number(num2)
    page.press_the_plus_button()
    assert page.get_result() == float(num1) + float(num2), 'Результат сложения  посчитан не верно'


@pytest.mark.parametrize('num1', [str(1.1), str(9.9), str(99.15), str(99.99), str(99.150), str(99.999)])
def test_sum_float(driver, num1, num2=1):
    """Проверка функции сложения с дробными числами"""
    page = MainPage(driver)
    page.input_to_first_number(num1)
    page.input_to_second_number(num2)
    page.press_the_plus_button()
    assert page.get_result() == float(num1) + float(num2), 'Результат сложения  посчитан не верно'


@pytest.mark.parametrize('num1', [6, 2])
@pytest.mark.parametrize('num2', [8, 3])
def test_div_positive(driver, num1, num2):
    """Проверка функции деления   целых чисел  """
    page = MainPage(driver)
    page.input_to_first_number(num1)
    page.input_to_second_number(num2)
    page.press_the_div_button()
    assert page.get_result() == float(num1) / float(num2), 'Результат деления  посчитан не верно'


@pytest.mark.parametrize('num1', [0, 11])
@pytest.mark.parametrize('num2', [9999999, 9999999999])
def test_div_many_numbers(driver, num2, num1):
    """Проверка функции деления   больших чисел """
    page = MainPage(driver)
    page.input_to_first_number(num1)
    page.input_to_second_number(num2)
    page.press_the_div_button()
    assert page.get_result() == float(num1) / float(num2), 'Результат деления  посчитан не верно'


@pytest.mark.parametrize('num1', [9, str(1.1), str(9.9), str(99.15), str(99.99), str(99.150), str(99.999)])
@pytest.mark.parametrize('num2', [str(1.9), 2])
def test_div_float(driver, num1, num2):
    """Проверка функции деления с дробными числами"""
    page = MainPage(driver)
    page.input_to_first_number(num1)
    page.input_to_second_number(num2)
    page.press_the_div_button()
    assert page.get_result() == float(num1) / float(num2), 'Результат деления  посчитан не верно'


@pytest.mark.parametrize('num1', [1, -9])
@pytest.mark.parametrize('num2', [-1, 9])
def test_div_negative(driver, num1, num2):
    """Проверка функции деления с отрицательными числами"""
    page = MainPage(driver)
    page.input_to_first_number(num1)
    page.input_to_second_number(num2)
    page.press_the_div_button()
    assert page.get_result() == float(num1) / float(num2), 'Результат деления  посчитан не верно'


@pytest.mark.parametrize('num1', [9, -9])
def test_div_by_0(driver, num1, num2=0):
    """Проверка деления  на 0 """
    page = MainPage(driver)
    page.input_to_first_number(num1)
    page.input_to_second_number(num2)
    page.press_the_div_button()
    assert 'Infinity' in page.get_result(), "Результат деления  ноль должен быть равен 'Infinity' или '-Infinity'"


@pytest.mark.parametrize('num1', [6, 2])
@pytest.mark.parametrize('num2', [8, 3])
def test_mult_positive(driver, num1, num2):
    """Проверка функции умножения   целых чисел  """
    page = MainPage(driver)
    page.input_to_first_number(num1)
    page.input_to_second_number(num2)
    page.press_the_mult_button()
    assert page.get_result() == float(num1) * float(num2), 'Результат умножения  посчитан не верно'


@pytest.mark.parametrize('num1', [0, 11])
@pytest.mark.parametrize('num2', [0, 9999999, 9999999999])
def test_mult_many_numbers(driver, num2, num1):
    """Проверка функции умножения   больших чисел """
    page = MainPage(driver)
    page.input_to_first_number(num1)
    page.input_to_second_number(num2)
    page.press_the_mult_button()
    assert page.get_result() == float(num1) * float(num2), 'Результат умножения  посчитан не верно'


@pytest.mark.parametrize('num1', [9, str(1.1), str(9.9), str(99.15), str(99.99), str(99.150), str(99.999)])
@pytest.mark.parametrize('num2', [str(1.9), 2])
def test_mult_float(driver, num1, num2):
    """Проверка функции умножения с дробными числами"""
    page = MainPage(driver)
    page.input_to_first_number(num1)
    page.input_to_second_number(num2)
    page.press_the_mult_button()
    assert page.get_result() == float(num1) * float(num2), 'Результат умножения  посчитан не верно'


@pytest.mark.parametrize('num1', [1, -9])
@pytest.mark.parametrize('num2', [-1, 9])
def test_mult_negative(driver, num1, num2):
    """Проверка функции умножения с отрицательными числами"""
    page = MainPage(driver)
    page.input_to_first_number(num1)
    page.input_to_second_number(num2)
    page.press_the_mult_button()
    assert page.get_result() == float(num1) * float(num2), 'Результат умножения  посчитан не верно'


