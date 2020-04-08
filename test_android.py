import pytest

from pages.main_page import MainPage


@pytest.mark.parametrize('num1', [9, 0])
@pytest.mark.parametrize('num2', [0, 9])
def test_dif_0_9(driver,  num2, num1):
    """Проверка функции вычитания с ислами 0 и 9"""
    page = MainPage(driver)
    page.minus(num1, num2)


@pytest.mark.parametrize('num1', [-9, 1])
@pytest.mark.parametrize('num2', [1, -9])
def test_dif_negative(driver,  num2, num1):
    """Проверка функции вычитания с отрицательными"""
    page = MainPage(driver)
    page.minus(num1, num2)


@pytest.mark.parametrize('num1', [6, 2])
@pytest.mark.parametrize('num2', [8, 3])
def test_dif_overflow_and_positive(driver,  num2, num1):
    """Проверка функции вычитания с переполнением десятка и без"""
    page = MainPage(driver)
    page.minus(num1, num2)


@pytest.mark.parametrize('num1', [0, 11])
@pytest.mark.parametrize('num2', [9999999, 9999999999])
def test_dif_many_numbers(driver,  num2, num1):
    """Проверка функции вычитания с большими числами"""
    page = MainPage(driver)
    page.minus(num1, num2)


@pytest.mark.parametrize('num1', [str(1.1), str(9.9), str(99.15), str(99.99), str(99.150), str(99.999)])
def test_dif_float(driver, num1, num2=1):
    """Проверка функции вычитания с дробными числами"""
    page = MainPage(driver)
    page.minus(num1, num2)


@pytest.mark.parametrize('num1', [9, 0])
@pytest.mark.parametrize('num2', [0, 9])
def test_sum_0_9(driver, num1, num2):
    """Проверка функции сложения с числами 0 и 9"""
    page = MainPage(driver)
    page.plus(num1, num2)


@pytest.mark.parametrize('num1', [-9, 1])
@pytest.mark.parametrize('num2', [1, -9])
def test_sum_negative(driver,  num2, num1):
    """Проверка функции сложения с отрицательными"""
    page = MainPage(driver)
    page.plus(num1, num2)


@pytest.mark.parametrize('num1', [6, 2])
@pytest.mark.parametrize('num2', [8, 3])
def test_sum_overflow_and_positive(driver, num1, num2):
    """Проверка функции сложения с переполнением десятка и без"""
    page = MainPage(driver)
    page.plus(num1, num2)


@pytest.mark.parametrize('num1', [9999999999, 11])
@pytest.mark.parametrize('num2', [11, 9999999999])
def test_sum_many_numbers(driver,  num2, num1):
    """Проверка функции сложения с большими числами"""
    page = MainPage(driver)
    page.plus(num1, num2)


@pytest.mark.parametrize('num1', [str(1.1), str(9.9), str(99.15), str(99.99), str(99.150), str(99.999)])
def test_sum_float(driver, num1, num2=1):
    """Проверка функции сложения с дробными числами"""
    page = MainPage(driver)
    page.plus(num1, num2)


@pytest.mark.parametrize('num1', [6, 2])
@pytest.mark.parametrize('num2', [8, 3])
def test_div_positive(driver, num1, num2):
    """Проверка функции деления   целых чисел  """
    page = MainPage(driver)
    page.division(num1, num2)


@pytest.mark.parametrize('num1', [0, 11])
@pytest.mark.parametrize('num2', [9999999, 9999999999])
def test_div_many_numbers(driver, num2, num1):
    """Проверка функции деления   больших чисел """
    page = MainPage(driver)
    page.division(num1, num2)


@pytest.mark.parametrize('num1', [9, str(1.1), str(9.9), str(99.15), str(99.99), str(99.150), str(99.999)])
@pytest.mark.parametrize('num2', [str(1.9), 2])
def test_div_float(driver, num1, num2):
    """Проверка функции деления с дробными числами"""
    page = MainPage(driver)
    page.division(num1, num2)


@pytest.mark.parametrize('num1', [1, -9])
@pytest.mark.parametrize('num2', [-1, 9])
def test_div_negative(driver, num1, num2):
    """Проверка функции деления с отрицательными числами"""
    page = MainPage(driver)
    page.division(num1, num2)


@pytest.mark.parametrize('num1', [9, -9])
def test_div_by_0(driver, num1):
    """Проверка деления  на 0 """
    page = MainPage(driver)
    page.data_entry_field_is_empty()
    page.should_be_all_buttons()
    page.divizion_by_zero(num1)


@pytest.mark.parametrize('num1', [6, 2])
@pytest.mark.parametrize('num2', [8, 3])
def test_mult_positive(driver, num1, num2):
    """Проверка функции умножения   целых чисел  """
    page = MainPage(driver)
    page.multiplication(num1, num2)


@pytest.mark.parametrize('num1', [0, 11])
@pytest.mark.parametrize('num2', [0, 9999999, 9999999999])
def test_mult_many_numbers(driver, num2, num1):
    """Проверка функции умножения   больших чисел """
    page = MainPage(driver)
    page.multiplication(num1, num2)


@pytest.mark.parametrize('num1', [9, str(1.1), str(9.9), str(99.15), str(99.99), str(99.150), str(99.999)])
@pytest.mark.parametrize('num2', [str(1.9), 2])
def test_mult_float(driver, num1, num2):
    """Проверка функции умножения с дробными числами"""
    page = MainPage(driver)
    page.multiplication(num1, num2)


@pytest.mark.parametrize('num1', [1, -9])
@pytest.mark.parametrize('num2', [-1, 9])
def test_mult_negative(driver, num1, num2):
    """Проверка функции умножения с отрицательными числами"""
    page = MainPage(driver)
    page.multiplication(num1, num2)


def test_after_clicking_on_reset_all_fields_are_cleared(driver):
    """Разные визуальные проверки"""
    page = MainPage(driver)
    page.data_entry_field_is_empty()  # Проверка того, что после того как зашли в приложение, поля ввода пустые
    page.digit_response1(1)  # Ввод чисел
    assert page.get_text_from_field1() != ' ', 'Поле 1 пустое после нажатия'
    page.digit_response2(1)  # Ввод чисел
    assert page.get_text_from_field2() != ' ', 'Поле 2 пустое после нажатия'
    page.reset_button()  # Проверка того, что после того как нажали на сброс, поля ввода пустые


@pytest.mark.parametrize('num1', ['%', 'gg'])
def test_input_is_not_int_or_float_1(driver, num1):
    """Вводим буквы и символы в поле 1"""
    page = MainPage(driver)
    page.digit_response1(num1)
    assert page.get_text_from_field1() == ' ', 'В Поле 1 ввелись буквы или символы'



@pytest.mark.parametrize('num2', ['gg', '%'])
def test_input_is_not_int_or_float_2(driver, num2):
    """Вводим буквы и символы в поле 2"""
    page = MainPage(driver)
    page.digit_response2(num2)
    assert page.get_text_from_field2() == ' ', 'В Поле 2 ввелись буквы или символы'