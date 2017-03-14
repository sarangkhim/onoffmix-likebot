"""
selenium, geckodriver, phantomjs
pip install selenium
"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
import time


def like_post(pid, eid, pw):
    #driver = webdriver.Firefox(executable_path='geckodriver.exe')
    driver = webdriver.PhantomJS(executable_path='phantomjs.exe')
    driver.get("http://onoffmix.com/event/" + str(pid))
    #delay = 1  # seconds

    #try:
    #    WebDriverWait(driver, delay).until(ec.presence_of_element_located(driver.find_element_by_link_text("로그인").click()))
    #except TimeoutException:
    #    print("Loading took too much time!")

    # click login link
    link = driver.find_element_by_link_text("로그인")
    link.click()
    time.sleep(3)

    # login onoffmix
    elem = driver.find_element_by_id("email")
    elem.send_keys(eid)
    elem = driver.find_element_by_id("pw")
    elem.send_keys(pw)
    elem.submit()
    time.sleep(3)

    # click like button
    driver.find_element_by_css_selector('.pin.event-action-pin').click()
    time.sleep(3)

    # close browser
    driver.quit()
    time.sleep(3)


if __name__ == "__main__":
    post_id = 93540
    email_ids = [str(n) + "zladkzk@naver.com" for n in range(10)]
    password = "qwe123"

    for email_id in email_ids:
        like_post(post_id, email_id, password)
