import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()

    driver.get("https://httpbin.qa-territory.online")
    time.sleep(1)

    link = driver.find_element(By.LINK_TEXT, "HTML Form")
    link.click()
    time.sleep(1)

    assert "/forms/post" in driver.current_url

    driver.back()
    time.sleep(1)

    assert driver.current_url == "https://httpbin.qa-territory.online/"

    driver.quit()
