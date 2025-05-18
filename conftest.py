import pytest
from selenium import webdriver
from configparser import ConfigParser

config = ConfigParser()
config.read("config/config.ini")


@pytest.fixture
def browser_name():
    return config.get("DEFAULT", "browser")


@pytest.fixture
def base_url():
    return config.get("DEFAULT", "base_url")


@pytest.fixture
def username():
    return config.get("DEFAULT", "username")


@pytest.fixture
def password():
    return config.get("DEFAULT", "password")


@pytest.fixture
def browser(browser_name):
    if browser_name.lower() == "chrome":
        driver = webdriver.Chrome()
    elif browser_name.lower() == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.maximize_window()
    yield driver
    driver.quit()
