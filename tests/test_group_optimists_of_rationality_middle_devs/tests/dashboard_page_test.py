from tests.test_group_optimists_of_rationality_middle_devs.locators.dashboard_page_locators import DashboardLocators
from tests.test_group_optimists_of_rationality_middle_devs.pages.dashboard_page import Dashboard


class TestDashboardPage:

    def test_006_04_03_Verify_that_the_subscribe_button_are_clickable_in_the_Pricing_and_limits_ection(self, driver):
        dashboard_page = Dashboard(driver, DashboardLocators.HEADER_DASHBOARD_LINK)
        dashboard_page.open_page()
        dashboard_page.subscribe_buttons_are_clickable()