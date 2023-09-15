from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchDriverException, NoSuchElementException
# NoSuchElementException`: это исключение возникает, когда WebDriver не может найти элемент на веб-странице.
# NoSuchDriverException`: это исключение возникает, когда WebDriver не может найти указанный драйвер. Тестов может быть огромное количество 100 или 1000, если эту строчку не прописать то при обновлении драйвера - тест выдаст ошибку и прекратит дальнейшее выполнение тестов, а с этой строчкеой не прекратит и продолжит
def test_site_visit():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    try:
        driver.find_element(By.CSS_SELECTOR, "div.login_logo")
        print("Элемент Лого найден")
    except NoSuchElementException:
        print("Элемент Лого не найден")

    except NoSuchDriverException:
        assert False
    assert True

def test_1_check_elements():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    try:
        driver.find_element(By.ID,"user-name")
        print("Элемент поле имени найден")
    except NoSuchDriverException:
        print("Элемент поле имени не найден")

def test_2_check_elements():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    try:
        driver.find_element(By.ID,"password")
        print("Элемент пароль найден")
    except NoSuchDriverException:
        print("Элемент пароль не найден")

