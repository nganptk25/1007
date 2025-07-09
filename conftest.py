import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

@pytest.fixture(scope="class")
def pages_login(request):
    request.cls.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    request.cls.driver.implicitly_wait(10)

    try:
        username_field = request.cls.driver.find_element(By.NAME, "username")
        password_field = request.cls.driver.find_element(By.NAME, "password")       
        submit_button = request.cls.driver.find_element(By.XPATH, "//button[@type='submit']")
    except NoSuchElementException: 
         raise Exception("One of the elements was not found on the page.")
    username_field.send_keys("Admin")
    password_field.send_keys("admin123")
    submit_button.click()
    request.cls.driver.implicitly_wait(10)

    for cookie in request.cls.driver.get_cookies():
        request.cls.session.cookies.set(cookie['name'], cookie['value'])