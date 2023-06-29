from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from selenium.webdriver.support.color import Color


URL_SOLAR_API = "https://openweathermap.org/api/solar-energy-prediction"
CITIES = ['New York', 'Los Angeles', 'Paris']
SEARCH_CITY_FIELD_LOCATOR = (By.CSS_SELECTOR, "input[placeholder='Search city']")
SEARCH_BUTTON_LOCATOR = (By.CSS_SELECTOR, "button[class ='button-round dark']")
SEARCH_1ST_OPTION_LOCATOR = (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:first-child span:first-child')
C_TEMP_LOCATOR = (By.CSS_SELECTOR, '.switch-container .option:nth-child(2)')
LINE_IN_8_DAYS_FORECAST_LOCATOR = (By.XPATH, "//div[@class='day-list-values']/div/span[contains(text(), '°C')]")
product_concept_title_locator = (By.CSS_SELECTOR, "#concept h2")
subscription_module_button = (By.CSS_SELECTOR, ".inner-footer-container div:first-of-type "
                                               ".footer-section:nth-child(2) p.section-heading")
QUALITY_INFO_PAGE = "https://openweathermap.org/accuracy-and-quality"
NWP_MODEL = (By.CSS_SELECTOR, ".col-sm-12 > ul:first-of-type")
CONTINUE_TO_PAYMENT_BUTTON = (By.CSS_SELECTOR, 'input[value ="Continue to payment"]')
CANT_BE_BLANK = (By.CSS_SELECTOR, '.help-block')
EXPECTED_NUMBER_OF_FIELDS = 7
URL_SUBSCRIPTION_BASE = 'https://home.openweathermap.org/subscriptions/unauth_subscribe/onecall_30/base'
MAIN_LOGO = (By.CSS_SELECTOR, 'img[src="/themes/openweathermap/assets/img/logo_white_cropped.png"]')
OUR_INITIATIVES_PAGE = 'https://openweathermap.org/our-initiatives'
MAIN_PAGE = 'https://openweathermap.org/'
HOW_TO_GET_ACCESS_LINK_LOCATOR = (By.XPATH, '//a[@href="#how"]')
HOW_TO_GET_ACCESS_TITLE_LOCATOR = (By.CSS_SELECTOR, "#how h2")
GUIDE_PAGE = "https://openweathermap.org/guide"
HISTORICAL_COLLECTION_MODULE = (By.CSS_SELECTOR, ".col-sm-12 ol ul:nth-of-type(2)")
LINK_HISTORICAL_ARCHIVE = (By.PARTIAL_LINK_TEXT, "archive")
CLICK_ALLOW_IN_STICK_FOOTER = (By.CLASS_NAME, 'stick-footer-panel__link')
URL_HISTORY_BULK = "https://openweathermap.org/history-bulk"
HISTORICAL_COLLECTION_LINKS = (By.CSS_SELECTOR, ".col-sm-12 ol ul:nth-of-type(2) a")
EXPECTED_LINK_COLOR_HEX = "#e96e50"
TITLE_NWP_MODEL_LOCATOR = (By.CSS_SELECTOR, '.col-sm-12 ol h2:nth-of-type(2)')
AGRICULTURE_ANALYTICS_TITLE_LOCATOR = (By.CSS_SELECTOR, ".section-content > .mobile-padding > div > h2")
URL_WEATHER_CONDITIONS = "https://openweathermap.org/weather-conditions"
WEATHER_ICONS = (By.XPATH, '//a[.="Weather icons"]')
ICONS_FOR_NIGHTTIME = (By.XPATH, '//td[contains(text(), "n.png")]')
EXPECTED_MINIMUM_ICONS_FOR_NIGHTTIME = 8


@pytest.mark.parametrize('city', CITIES)
def test_TC_001_04_01_visibility_of_8_lines_in_8_day_forecast_block(driver, open_and_load_main_page, city):
    """Checking if all 8 lines are visible in 8-day forecast block"""
    search_city_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(SEARCH_CITY_FIELD_LOCATOR))
    search_city_field.send_keys(city)
    search_button = driver.find_element(*SEARCH_BUTTON_LOCATOR)
    search_button.click()
    search_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(SEARCH_1ST_OPTION_LOCATOR))
    search_option.click()
    c_temp = driver.find_element(*C_TEMP_LOCATOR)
    c_temp.click()
    lines = driver.find_elements(*LINE_IN_8_DAYS_FORECAST_LOCATOR)
    for line in lines:
        assert line.is_displayed()


def test_TC_005_10_02_visibility_of_Product_concept_article_title(driver):
    driver.get(URL_SOLAR_API)
    product_concept_title = driver.find_element(*product_concept_title_locator)
    assert product_concept_title.is_displayed()



def test_TC_003_05_01_subscription_module_title_displayed(driver, open_and_load_main_page):
    subscription_title = driver.find_element(*subscription_module_button)
    driver.execute_script("arguments[0].click();", subscription_title)
    assert subscription_title.is_displayed()



def test_001_017_01_visibility_of_nwp_block(driver):
    driver.get(QUALITY_INFO_PAGE)
    nwp = driver.find_element(*NWP_MODEL)
    assert nwp.is_displayed()


def test_TC_018_01_02_Verify_error_messages_for_empty_required_fields(driver):
    driver.get(URL_SUBSCRIPTION_BASE)
    driver.find_element(*CONTINUE_TO_PAYMENT_BUTTON).click()
    error_messages = driver.find_elements(*CANT_BE_BLANK)
    checks = 0
    for i in error_messages:
        assert i.is_displayed()
        checks += 1
    assert checks == EXPECTED_NUMBER_OF_FIELDS

def test_002_01_11_verify_main_logo(driver):
    driver.get(OUR_INITIATIVES_PAGE)
    m_logo = driver.find_element(*MAIN_LOGO)
    m_logo.click()
    response = requests.get(MAIN_PAGE)
    assert response.status_code == 200


def test_TC_005_10_03_correct_redirection_for_how_to_get_access_link(driver):
    """Checking for correct redirection when clicking on How to get access link from the side menu"""
    driver.get(URL_SOLAR_API)
    how_to_get_access_link = driver.find_element(*HOW_TO_GET_ACCESS_LINK_LOCATOR)
    how_to_get_access_link.click()
    how_to_get_access_title = driver.find_element(*HOW_TO_GET_ACCESS_TITLE_LOCATOR)
    assert how_to_get_access_title.is_displayed()


def test_TC_021_01_01_visibility_of_agriculture_analytics_link(driver, open_and_load_main_page, wait):
    assert driver.find_element(*AGRICULTURE_ANALYTICS_TITLE_LOCATOR).is_displayed()



def test_TC_004_08_01_historical_collection_block_visibility(driver):
    driver.get(GUIDE_PAGE)
    historical_collection = driver.find_element(*HISTORICAL_COLLECTION_MODULE)
    driver.execute_script("arguments[0].scrollIntoView(true);", historical_collection)
    assert historical_collection.is_displayed(), "The Historical Weather collection is not displaying"


def test_TC_004_08_02_link_to_history_archive_is_clickable(driver):
    driver.get(GUIDE_PAGE)
    archive_link = driver.find_element(*LINK_HISTORICAL_ARCHIVE)
    actions = ActionChains(driver)
    actions.move_to_element(archive_link).perform()
    assert archive_link.is_enabled(), "The link is not clickable"



def test_TC_004_08_03_historical_collection_link_redirects_correctly(driver):
    driver.get(GUIDE_PAGE)
    driver.find_element(*CLICK_ALLOW_IN_STICK_FOOTER).click()
    driver.find_element(*LINK_HISTORICAL_ARCHIVE).click()
    assert driver.current_url == URL_HISTORY_BULK



def test_TC_004_08_03_verify_all_links_same_color(driver):
    driver.get(GUIDE_PAGE)
    all_links = driver.find_elements(*HISTORICAL_COLLECTION_LINKS)
    for link in all_links:
        link_color_rgba = link.value_of_css_property("color")
        link_color_hex = Color.from_string(link_color_rgba).hex
        assert link_color_hex == EXPECTED_LINK_COLOR_HEX, "The links' colors do not match the standard"


def test_TC_004_02_01_visibility_of_title_of_article(driver):
    driver.get(GUIDE_PAGE)
    title_nwp_model = driver.find_element(*TITLE_NWP_MODEL_LOCATOR)
    assert title_nwp_model.is_displayed()


def test_TC_001_10_03_verify_count_of_icons_for_nighttime(driver):
    driver.get(URL_WEATHER_CONDITIONS)
    weather_icons = driver.find_element(*WEATHER_ICONS)
    weather_icons.click()
    actual_icons_for_nighttime = driver.find_elements(*ICONS_FOR_NIGHTTIME)
    assert len(actual_icons_for_nighttime) >= EXPECTED_MINIMUM_ICONS_FOR_NIGHTTIME



from selenium.webdriver.common.action_chains import ActionChains

URL = 'https://openweathermap.org/'
cities = ['New York', 'Los Angeles', 'Paris']
load_div = (By.CSS_SELECTOR, 'div.owm-loader-container > div')
search_dropdown = (By.CSS_SELECTOR, 'ul.search-dropdown-menu li')
search_dropdown_option = (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)')
search_city_field = (By.CSS_SELECTOR, "input[placeholder='Search city']")
search_button = (By.CSS_SELECTOR, "button[class ='button-round dark']")
displayed_city = (By.CSS_SELECTOR, '.grid-container.grid-4-5 h2')
city = "Los Angeles, US"


def test_should_open_given_link(driver):
    driver.get(URL)
    assert 'openweathermap' in driver.current_url


def test_check_page_title(driver):
    driver.get(URL)
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'


@pytest.mark.parametrize('city', cities)
def test_fill_search_city_field(driver, city):
    driver.get(URL)
    wait = WebDriverWait(driver, 15)
    wait.until_not(EC.presence_of_element_located(load_div))
    search_city_input = driver.find_element(*search_city_field)
    search_city_input.send_keys(city)
    driver.find_element(*search_button).click()
    wait.until(EC.element_to_be_clickable(search_dropdown_option)).click()
    expected_city = city
    wait.until(EC.text_to_be_present_in_element(displayed_city, city))
    actual_city = driver.find_element(*displayed_city).text
    assert expected_city in actual_city


@pytest.mark.parametrize('city', cities)
def test_all_dropdown_options_should_contain_valid_city(driver, city):
    driver.get(URL)
    wait = WebDriverWait(driver, 15)
    wait.until_not(EC.presence_of_element_located(load_div))
    search_city_input = driver.find_element(*search_city_field)
    search_city_input.send_keys(city)
    driver.find_element(*search_button).click()
    options = driver.find_elements(*search_dropdown)
    for option in options:
        assert city in option.text


def test_link_in_nav_bar_Partners(driver):
    driver.get(URL)
    wait = WebDriverWait(driver, 15)
    wait.until_not(EC.presence_of_element_located(load_div))
    element = driver.find_element(By.CSS_SELECTOR, "#desktop-menu>ul>li:nth-child(8)>a")
    action_chains = ActionChains(driver)
    action_chains.move_to_element(element)
    driver.execute_script("arguments[0].click();", element)
    nav_bar_partners_title_text = driver.find_element(By.CSS_SELECTOR, ".breadcrumb-title").text
    assert nav_bar_partners_title_text == "Partners and solutions"


def test_check_meteorological_conditions_are_displayed(driver):
    driver.get(URL)
    WebDriverWait(driver, 15).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    search_city_field_1 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "input[placeholder='Search city']")))
    search_city_field_1.send_keys(city)
    search_button_1 = driver.find_element(By.CSS_SELECTOR, "button[class ='button-round dark']")
    search_button_1.click()
    search_option = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:first-child span:first-child')))
    search_option.click()
    WebDriverWait(driver, 15).until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, '.grid-container.grid-4-5 h2'), city))
    displayed_city_1 = driver.find_element(By.CSS_SELECTOR, '.grid-container.grid-4-5 h2').text
    assert displayed_city_1 == city
    assert driver.find_element(By.CSS_SELECTOR, '.wind-line').is_displayed()
    assert driver.find_element(By.XPATH, '//span[text()="Humidity:"]').is_displayed()
    assert driver.find_element(By.XPATH, "//span[text()='Visibility:']").is_displayed()
    assert driver.find_element(By.CSS_SELECTOR, "li .icon-pressure").is_displayed()
    assert driver.find_element(By.XPATH, '//span[text()="Dew point:"] ').is_displayed()


def test_api_recommended_version(driver):
    driver.get(URL)
    WebDriverWait(driver, 15).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    button_api = WebDriverWait(driver, 35).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#desktop-menu>ul>li:nth-child(2)>a")))
    action_chains = ActionChains(driver)
    action_chains.move_to_element(button_api)
    driver.execute_script("arguments[0].click();", button_api)
    api_recommended_version = driver.find_element(By.XPATH, '//p/a[contains(text(), "One Call API 3.0")]').text
    assert api_recommended_version == "One Call API 3.0"


def test_image_open_weather(driver):
    driver.get(URL)
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    assert driver.find_element(By.XPATH,
                               "//img[@src='/themes/openweathermap/assets/img/logo_white_cropped.png']").is_displayed()


def test_check_header_name(driver):
    driver.get(URL)
    WebDriverWait(driver, 15).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    assert driver.find_element(By.XPATH, "/html/body/main/div[1]/div/div/div[1]/div/h1/span").text == 'OpenWeather'


def test_change_temp(driver):
    driver.get(URL)
    WebDriverWait(driver, 15).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    f_button = driver.find_element(By.CSS_SELECTOR, ".switch-container > div:nth-of-type(3)")
    f_button.click()
    assert driver.find_element(By.XPATH, "//div[@class='current-temp']/span[contains(text(), '°F')]").is_displayed()




def test_temperature_f_conversion(driver):
    driver.get(URL)
    WebDriverWait(driver, 15).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    search_city_field = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "input[placeholder='Search city']")))
    search_city_field.send_keys(city)
    search_button = driver.find_element(By.CSS_SELECTOR, "button[class ='button-round dark']")
    search_button.click()
    search_option = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:first-child span:first-child')))
    search_option.click()
    WebDriverWait(driver, 15).until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, '.grid-container.grid-4-5 h2'), city))
    f_temp = driver.find_element(By.CSS_SELECTOR, '.switch-container .option:nth-child(3)')
    f_temp.click()
    assert driver.find_element(By.XPATH, "//div[@class='current-temp']/span[contains(text(), '°F')]").is_displayed()


def test_temperature_c_conversion(driver):
    driver.get(URL)
    WebDriverWait(driver, 15).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    search_city_field = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "input[placeholder='Search city']")))
    search_city_field.send_keys(city)
    search_button = driver.find_element(By.CSS_SELECTOR, "button[class ='button-round dark']")
    search_button.click()
    search_option = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:first-child span:first-child')))
    search_option.click()
    WebDriverWait(driver, 15).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    f_temp = driver.find_element(By.CSS_SELECTOR, '.switch-container .option:nth-child(2)')
    f_temp.click()
    assert driver.find_element(By.XPATH, "//div[@class='current-temp']/span[contains(text(), '°C')]").is_displayed()

def test_return_homepage(driver):
    driver.get("https://home.openweathermap.org/users/sign_in")
    driver.find_element(By.CSS_SELECTOR, ".logo").click()
    assert driver.current_url == URL