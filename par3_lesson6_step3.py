import math
import time
from selenium import webdriver
import pytest



@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestUfo():

    @pytest.mark.parametrize('number', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
    def test_correct_find_field(self, browser, number):
        browser.get(f'https://stepik.org/lesson/{number}/step/1')
        answer = str(math.log(int(time.time() + 0.3)))
        browser.find_element_by_css_selector('textarea.string-quiz__textarea').send_keys(answer)
        browser.find_element_by_css_selector('button.submit-submission').click()
        optionalField = browser.find_element_by_css_selector('pre.smart-hints__hint').text
        assert optionalField == "Correct!", f"{optionalField}"
