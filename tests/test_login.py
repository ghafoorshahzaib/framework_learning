# from pages.login_page import LoginPage
# from utils.logger import get_logger
#
# logger = get_logger(__name__)
#
#
# def test_valid_login(browser, base_url, username, password):
#     logger.info("Starting test_valid_login")
#     browser.get(base_url)
#     logger.debug("Navigated to login page: %s", browser.current_url)
#     page = LoginPage(browser)
#     page.login(username, password)
#     logger.info("Login attempt completed")
#     welcome_text = page.get_welcome_text()
#     logger.debug("Welcome text: %s", welcome_text)
#     assert "Total Organizations" in welcome_text
#     logger.info("Test passed: Welcome text verified")
#
#
# def test_invalid_login(browser, base_url):
#     browser.get(base_url)
#     page = LoginPage(browser)
#     page.login("wrong_user@example.com", "wrong_pass")
#     error_message = page.get_error_message()
#     assert "Error" in error_message
#
#
# def test_empty_username(browser, base_url):
#     browser.get(base_url)
#     page = LoginPage(browser)
#     page.login("", "somepassword")
#     error_message = page.get_validation_error()
#     assert "Please enter your email address" in error_message

from pages.login_page import LoginPage
from utils.logger import get_logger

logger = get_logger(__name__)


def test_valid_login(browser, base_url, username, password):
    logger.info("Starting test_valid_login")
    browser.get(base_url)
    logger.debug("Navigated to login page: %s", browser.current_url)
    page = LoginPage(browser)
    page.login(username, password)
    logger.info("Login attempt completed")
    welcome_text = page.get_welcome_text()
    logger.debug("Welcome text: %s", welcome_text)
    assert "Total Organizations" in welcome_text
    logger.info("Test passed: Welcome text verified")


def test_invalid_login(browser, base_url):
    logger.info("Starting test_invalid_login")
    browser.get(base_url)
    logger.debug("Navigated to login page: %s", browser.current_url)
    page = LoginPage(browser)
    page.login("wrong_user@example.com", "wrong_pass")
    logger.info("Login with invalid credentials attempted")
    error_message = page.get_error_message()
    logger.debug("Error message: %s", error_message)
    assert error_message is not None, "Error message not found"
    assert "Error" in error_message, f"Expected 'Error' in message, got: {error_message}"
    logger.info("Test passed: Invalid login detected")


def test_empty_username(browser, base_url):
    logger.info("Starting test_empty_username")
    browser.get(base_url)
    logger.debug("Navigated to login page: %s", browser.current_url)
    page = LoginPage(browser)
    page.login("", "somepassword")
    logger.info("Login with empty username attempted")
    error_message = page.get_validation_error()
    logger.debug("Validation error: %s", error_message)
    assert error_message is not None, "Validation error not found"
    assert "Please enter your email address" in error_message, f"Expected 'Please enter your email address', got: {error_message}"
    logger.info("Test passed: Empty username validation detected")
