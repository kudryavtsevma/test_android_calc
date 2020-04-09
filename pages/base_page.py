from selenium.common.exceptions import NoSuchElementException



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

    def get_text_from_element(self, how, what):
        text = self.driver.find_element(how, what).text
        return text
