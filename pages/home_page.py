#it is to locate elements & perform actions

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class HomePage(BasePage):

    add_note_btn = (
        By.XPATH,
        "//button[@data-testid='add-new-note']"
    )

    title_input = (
        By.XPATH,
        "//input[@data-testid='note-title']"
    )

    description_input = (
        By.XPATH,
        "//textarea[@data-testid='note-description']"
    )

    category_dropdown = (
        By.XPATH,
        "//select[@data-testid='note-category']"
    )

    save_btn = (
        By.XPATH,
        "//button[@data-testid='note-submit']"
    )
#to create note using ui
    def create_note(self, title, description):

        add_button = WebDriverWait(
            self.driver,
            30
        ).until(
            EC.presence_of_element_located(
                self.add_note_btn
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            add_button
        )

        self.driver.execute_script(
            "arguments[0].click();",
            add_button
        )

        self.type(
            self.title_input,
            title
        )

        self.type(
            self.description_input,
            description
        )

        category = self.find(
            self.category_dropdown
        )

        category.send_keys("Home")

        self.click(self.save_btn)
#for note visible
    def is_note_visible(self, title):

        return title in self.driver.page_source
#for note not visible
    def is_note_not_visible(self, title):

        return title not in self.driver.page_source