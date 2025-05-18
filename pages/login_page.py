# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from utils.logger import get_logger
#
# logger = get_logger(__name__)
#
#
# class LoginPage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.username_input = (By.ID, "email")
#         self.password_input = (By.ID, "password")
#         self.login_button = (By.CSS_SELECTOR, "button[type='submit']")
#         self.welcome_message = (By.XPATH, "//div[contains(text(), 'Total Organizations')]")
#
#     def login(self, username, password):
#         WebDriverWait(self.driver, 10).until(
#             EC.presence_of_element_located(self.username_input)
#         ).send_keys(username)
#         self.driver.find_element(*self.password_input).send_keys(password)
#         self.driver.find_element(*self.login_button).click()
#         logger.info("Login button clicked")
#
#     def get_welcome_text(self):
#         WebDriverWait(self.driver, 10).until(
#             EC.visibility_of_element_located(self.welcome_message)
#         )
#         return self.driver.find_element(*self.welcome_message).text
#         logger.debug("Welcome text retrieved: %s", welcome_text)
#         return welcome_text
#
#     def get_error_message(self):
#         try:
#             element = WebDriverWait(self.driver, 10).until(
#                 EC.visibility_of_element_located((By.CLASS_NAME, "ant-notification-notice-message"))
#             )
#             return element.text
#         except Exception as e:
#             print(f"Error not found: {e}")
#             return None
#
#     def get_validation_error(self):
#         try:
#             element = WebDriverWait(self.driver, 10).until(
#                 EC.visibility_of_element_located((By.CLASS_NAME, "ant-form-item-explain-error"))
#             )
#             return element.text
#         except Exception as e:
#             print(f"Validation error not found: {e}")
#             return None
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger

logger = get_logger(__name__)

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "email")
        self.password_input = (By.ID, "password")
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")
        self.welcome_message = (By.XPATH, "//div[contains(text(), 'Total Organizations')]")

    def login(self, username, password):
        logger.info("Attempting to log in with username: %s", username)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.username_input)
        ).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
        logger.info("Login button clicked")

    def get_welcome_text(self):
        logger.debug("Retrieving welcome text")
        welcome_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.welcome_message)
        )
        welcome_text = welcome_element.text
        logger.debug("Welcome text retrieved: %s", welcome_text)
        return welcome_text

    def get_error_message(self):
        logger.debug("Checking for error message")
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "ant-notification-notice-message"))
            )
            error_text = element.text
            logger.debug("Error message retrieved: %s", error_text)
            return error_text
        except Exception as e:
            logger.error("Error message not found: %s", str(e))
            return None

    def get_validation_error(self):
        logger.debug("Checking for validation error")
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "ant-form-item-explain-error"))
            )
            validation_error = element.text
            logger.debug("Validation error retrieved: %s", validation_error)
            return validation_error
        except Exception as e:
            logger.error("Validation error not found: %s", str(e))
            return None