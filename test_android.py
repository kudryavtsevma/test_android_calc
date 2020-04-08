import pytest
from .pages.main_page import MainPage


class TestDifferense:
    """Проверка функции вычитания с разными числами"""
    @pytest.mark.parametrize('num1', [0, 1, str(1.1), str(1.9), str(1.12),str(1.985), 99, 9999,  999999, 9999999,
                                      99999999, 999999999])
    @pytest.mark.parametrize('num2', [0, 1, str(1.1), str(1.9), str(1.12),str(1.985), 99, 9999,  999999, 9999999,
                                      99999999, 999999999])
    def test_dif(self, driver, num1, num2):
        page = MainPage(driver)
        page.minus(num1, num2)

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        page = MainPage(driver)
        page.reset_button()


class TestSum:
    """Проверка функции сложения с разными числами"""
    @pytest.mark.parametrize('num1', [0, 1, str(1.1), str(1.9), str(1.12),str(1.985), 99, 9999,  999999, 9999999,
                                      99999999, 999999999])
    @pytest.mark.parametrize('num2', [0, 1, str(1.1), str(1.9), str(1.12),str(1.985), 99, 9999,  999999, 9999999,
                                      99999999, 999999999])
    def test_sum0(self, driver, num1, num2):
        page = MainPage(driver)
        page.plus(num1, num2)

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        page = MainPage(driver)
        page.reset_button()


class TestDivision:
    """Проверка деления"""
    @pytest.mark.parametrize('num1', [0, 1, str(1.1), str(1.9), str(1.12),str(1.985), 99, 9999,  999999, 9999999,
                                      99999999, 999999999])
    @pytest.mark.parametrize('num2', [1, str(1.1), str(1.9), str(1.12),str(1.985), 99, 9999,  999999, 9999999,
                                      99999999, 999999999])
    def test_div(self, driver, num1, num2):
        """Проверка деления с разными числами. Деление на 0 не проверяется"""
        page = MainPage(driver)
        page.division(num1, num2)

    @pytest.mark.parametrize('num1', [1, str(1.1), str(1.9), str(1.12),str(1.985), 99, 9999,  999999, 9999999,
                                      99999999, 999999999])
    def test_div_by_0(self,driver, num1):
        """Проверка деления  на 0 """
        page = MainPage(driver)
        page.data_entry_field_is_empty()
        page.should_be_all_buttons()
        page.divizion_by_zero(num1)

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        page = MainPage(driver)
        page.reset_button()


class TestMultiplication:
    """Проверка функции умножения с разными числами"""
    @pytest.mark.parametrize('num1', [0, 1, str(1.1), str(1.9), str(1.12),str(1.985), 99, 9999,  999999, 9999999,
                                      99999999, 999999999])
    @pytest.mark.parametrize('num2', [0, 1, str(1.1), str(1.9), str(1.12),str(1.985), 99, 9999,  999999, 9999999,
                                      99999999, 999999999])
    def test_mult(self, driver, num2, num1):
        page = MainPage(driver)
        page.multiplication(num1, num2)

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        page = MainPage(driver)
        page.reset_button()


class TestVisuality:
    def test_after_clicking_on_reset_all_fields_are_cleared(self, driver):
        page = MainPage(driver)
        page.data_entry_field_is_empty()  # Проверка того, что после того как зашли в приложение, поля ввода пустые
        page.digit_response1()
        page.digit_response2()
        page.reset_button()  # Проверка того, что после того как нажали на сброс, поля ввода пустые



