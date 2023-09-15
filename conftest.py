import pytest
from selenium import webdriver


@pytest.fixture(scope="session")     # Декоратор говорит что эта функция является фикстурой
def browser():
    driver = webdriver.Chrome()
    yield driver                  # примерно как return но не завершает функцию
    driver.quit()


#@pytest.fixture(scope="session")     # Декоратор говорит что эта функция является фикстурой
#def browser():
    ###driver.quit()
###driver.quit()
###driver.quit()