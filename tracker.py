import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys

import config


def decorator(url, failure_text):
    def real_decorator(function):
        def wrapper():
            driver = webdriver.PhantomJS(config.PHANTOMJS_PATH)
            driver.get(url)
            try: text = function(driver)
            except NoSuchElementException or TimeoutException: text = failure_text
            driver.quit()
            return text
        return wrapper
    return real_decorator


@decorator(config.UKRPOSHTA_URL, config.UKRPOSHTA_FAIL)
def ukrposhta(driver):
    field = driver.find_element_by_id(config.UKRPOSHTA_FIELD_ID)
    field.send_keys(config.UKRPOSHTA_ID)
    field.send_keys(Keys.RETURN)
    driver.implicitly_wait(10)
    at_time = driver.find_element_by_id(config.UKRPOSHTA_TIME_ID).text
    answer = driver.find_element_by_id(config.UKRPOSHTA_ANSWER_ID).text
    return '{}: {}'.format(at_time, answer)


@decorator(config.POSHTASTAT_URL, config.POSHTASTAT_FAIL)
def poshta_stat(driver):
    if config.POSHTASTAT_SEARCH_STRING in driver.page_source:
        xpath = "//*[contains(text(), '{}')]/following-sibling::td".format(config.POSHTASTAT_SEARCH_STRING)
        td = driver.find_element_by_xpath(xpath)
        return td.text
    return config.POSHTASTAT_NO_IMPORT

while True:
    print(ukrposhta(), poshta_stat())
    time.sleep(300)
