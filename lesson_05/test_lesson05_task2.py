from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")

    original_url = driver.current_url

    input_field = driver.find_element(By.NAME, "custname")
    input_field.send_keys("Кирилл")

    submit_button = driver.find_element(By.XPATH, "//button[text()='Submit']")
    submit_button.click()

    wait = WebDriverWait(driver, 10)
    wait.until(lambda driver: driver.current_url != original_url)

    assert driver.current_url != original_url

    driver.quit()
