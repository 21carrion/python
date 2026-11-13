from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    user1_cookie_name = "SESSION"
    user1_cookie_value = "M2ZjMzA5MzAtOWQ2OS00ODg0LThlZTctZTJlYmRkYWE2NDE5"
    user1_profile_url = "https://gitflic.ru/user/carrion_1"

    user2_cookie_name = "SESSION"
    user2_cookie_value = "Y2ZmMWY1NGYtMzM2Yi00ZThjLWI3Y2MtZWNlZjVmYTZiMGEy"
    user2_profile_url = "https://gitflic.ru/user/carrion_3"

    driver.get("https://gitflic.ru/")

    driver.add_cookie({
        "name": user1_cookie_name,
        "value": user1_cookie_value,
        "domain": ".gitflic.ru"
    })

    driver.refresh()

    wait.until(lambda d: d.current_url == user1_profile_url)
    url_user1 = driver.current_url

    driver.delete_all_cookies()

    driver.add_cookie({
        "name": user2_cookie_name,
        "value": user2_cookie_value,
        "domain": ".gitflic.ru"
    })

    driver.refresh()

    wait.until(lambda d: d.current_url == user2_profile_url)
    url_user2 = driver.current_url

    assert url_user1 != url_user2

    driver.quit()
