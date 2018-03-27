from another_approach.pages.base_page import BasePage

class FirstPage(BasePage):
    @property
    def username_field(self):
        return self.driver.find_element_by_id("edit_user")

    @property
    def password_field(self):
        return self.driver.find_element_by_id("edit_pass")

    @property
    def submit_button(self):
        return self.driver.find_element_by_id('#LoginForm > input[type="submit"]')

    def is_this_page(self):
        return self.is_element_visible(By.ID, "LoginForm")

