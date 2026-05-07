#it is to locate elements & perform actions

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    email = (By.XPATH, "//input[@data-testid='login-email']")
    password = (By.XPATH, "//input[@data-testid='login-password']")
    login_btn = (By.XPATH, "//button[@data-testid='login-submit']")
#to login with ui
    def login(self, user, pwd):

        self.type(self.email, user)
        self.type(self.password, pwd)
        self.click(self.login_btn)