from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_validation():
    driver = webdriver.Safari()
    wait = WebDriverWait(driver, 10)

    url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    driver.get(url)

    fields = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    for name, value in fields.items():
        element = wait.until(
            EC.presence_of_element_located((By.NAME, name))
        )
        element.clear()
        element.send_keys(value)

    submit_btn = driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']"
    )
    driver.execute_script("arguments[0].click();", submit_btn)

    zip_field = wait.until(
        EC.presence_of_element_located((By.ID, "zip-code"))
    )
    zip_color = zip_field.value_of_css_property("background-color")

    assert zip_color == "rgba(248, 215, 218, 1)", zip_color

    for name in fields.keys():
        field = driver.find_element(By.ID, name)
        field_color = field.value_of_css_property("background-color")

        assert field_color == "rgba(209, 231, 221, 1)", name

    driver.quit()
