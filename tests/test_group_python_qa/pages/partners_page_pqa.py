from pages.base_page import BasePage
from tests.test_group_python_qa.locators.locators import PartnersAndSolutionsLocators
from tests.test_group_python_qa.links.links_all_pages import WEATHER_INDICATOR_PAGE


class PartnersAndSolutions(BasePage):
    locator = PartnersAndSolutionsLocators()

    def check_correct_redirection(self):
        assert WEATHER_INDICATOR_PAGE == self.driver.current_url, "Incorrect page"

    def link_see_library_visibility(self, wait):
        self.element_is_displayed(self.locator.LINK_SEE_LIBRARY, wait)