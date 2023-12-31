from pages.base_page import BasePage
from tests.test_group_python_qa.locators.locators import GuidePageLocators
from selenium.webdriver.support.color import Color

class GuidePage(BasePage):
    URL_GUIDE_PAGE = "https://openweathermap.org/guide"
    URL_HISTORY_BULK = "https://openweathermap.org/history-bulk"
    locators = GuidePageLocators()

    def historical_collection_block_visibility(self):
        self.driver.get(self.URL_GUIDE_PAGE)
        historical_collection = self.driver.find_element(*self.locators.HISTORICAL_COLLECTION_MODULE)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", historical_collection)
        assert historical_collection.is_displayed(), "The Historical Weather collection is not displaying"

