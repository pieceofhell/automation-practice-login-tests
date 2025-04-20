import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    driver = webdriver.Chrome()  # ou Firefox, Edge, etc.
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
