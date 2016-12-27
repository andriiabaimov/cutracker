import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys

import config


def get_driver(url, failure_text):
    def decorator(function):
        def wrapper():
            driver = webdriver.PhantomJS(config.PHANTOMJS_PATH)
            driver.get(url)
            try:
                text = function(driver)
            except NoSuchElementException or TimeoutException:
                text = failure_text
            driver.quit()
            return text
        return wrapper
    return decorator


@get_driver(config.UKRPOSHTA_URL, config.UKRPOSHTA_FAIL)
def ukrposhta(driver):
    field = driver.find_element_by_id(config.UKRPOSHTA_FIELD_ID)
    field.send_keys(config.UKRPOSHTA_ID)
    field.send_keys(Keys.RETURN)
    driver.implicitly_wait(config.UKRPOSHTA_WAIT)
    at_time = driver.find_element_by_id(config.UKRPOSHTA_TIME_ID).text
    answer = driver.find_element_by_id(config.UKRPOSHTA_ANSWER_ID).text
    return '{}: {}'.format(at_time, answer)


@get_driver(config.POSHTASTAT_URL, config.POSHTASTAT_FAIL)
def poshta_stat(driver):
    xpath = "//*[contains(text(), '{}')]/following-sibling::td".format(config.POSHTASTAT_LAST_UPDATE)
    td = driver.find_element_by_xpath(xpath)
    at_time = td.text
    answer = config.POSHTASTAT_NO_IMPORT
    if config.POSHTASTAT_SEARCH_STRING in driver.page_source:
        xpath = "//*[contains(text(), '{}')]/following-sibling::td".format(config.POSHTASTAT_SEARCH_STRING)
        td = driver.find_element_by_xpath(xpath)
        answer = '{} {}'.format(config.POSHTASTAT_IMPORT, td.text)
    return '{}: {}'.format(at_time, answer)

while True:
    print(ukrposhta(), poshta_stat())
    time.sleep(config.REQUEST_EVERY_SECONDS)
