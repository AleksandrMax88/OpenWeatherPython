import time
from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://openweathermap.org/'
STUDENT_INITIATIVE_URL = 'https://openweathermap.org/our-initiatives/student-initiative'
search_city_field_locator = (By.CSS_SELECTOR, "input[placeholder='Search city']")
search_button_locator = (By.CSS_SELECTOR, "button[class ='button-round dark']")
search_dropdown_option = (By.CSS_SELECTOR, "ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)")
graphic_hourly_forecast_locator = (By.CSS_SELECTOR, "canvas[id=chart-component]")
weather_items_locator = (By.CSS_SELECTOR, "ul.weather-items")
weather_item_locator = (By.CSS_SELECTOR, 'ul.weather-items li:nth-child(1)')
website_link_locator = (By.CSS_SELECTOR, 'section#terms.anchor_el a[href="/"]')
ask_us_popup_locator = (By.CSS_SELECTOR, 'section#terms.anchor_el a[href="mailto:info@openweathermap.org"]')

def test_tc_001_08_01_graphic_hourly_forecast_is_displayed(driver, open_and_load_main_page, wait):
    driver.get(URL)
    graphic_hourly_forecast = driver.find_element(*graphic_hourly_forecast_locator)
    assert graphic_hourly_forecast.is_displayed()


def test_tc_001_08_02_weather_items_are_displayed(driver, open_and_load_main_page, wait):
    driver.get(URL)
    weather_items = driver.find_elements(*weather_item_locator)
    for weather_item in weather_items:
        assert weather_item.is_displayed()

def test_TC_010_02_06_verify_website_link_redirects_to_main_page(driver, open_and_load_main_page, wait):
    driver.get(STUDENT_INITIATIVE_URL)
    website_link = driver.find_element(*website_link_locator)
    driver.execute_script("arguments[0].click();", website_link)
    assert driver.current_url == URL

def test_tc_010_02_07_verify_correct_redirection_to_popup_window(driver, open_and_load_main_page, wait):
    driver.get(STUDENT_INITIATIVE_URL)
    ask_us_popup = driver.find_element(*ask_us_popup_locator)
    assert ask_us_popup.is_enabled() and ask_us_popup.is_displayed()


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.common.action_chains import ActionChains

URL = 'https://openweathermap.org/'

cities = ['New York', 'Los Angeles', 'Paris']
load_div = (By.CSS_SELECTOR, 'div.owm-loader-container > div')
search_dropdown = (By.CSS_SELECTOR, 'ul.search-dropdown-menu li')
search_dropdown_option = (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)')
search_city_field = (By.CSS_SELECTOR, "input[placeholder='Search city']")
search_button = (By.CSS_SELECTOR, "button[class ='button-round dark']")
displayed_city = (By.CSS_SELECTOR, '.grid-container.grid-4-5 h2')
sign_in_link = (By.CSS_SELECTOR, '.user-li a')
pricing_link = (By.CSS_SELECTOR, '#desktop-menu a[href="/price"]')
price_page_title = (By.CSS_SELECTOR, "h1[class='breadcrumb-title']")
accept_cookies = (By.CSS_SELECTOR, 'button.stick-footer-panel__link')


def test_should_open_given_link(driver):
    driver.get(URL)
    assert 'openweathermap' in driver.current_url


def test_check_page_title(driver):
    driver.get(URL)
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'


def test_section_where_to(driver):
    driver.get(URL)
    element_section_where_to_h1 = driver.find_element(By.CSS_SELECTOR, ".mobile-padding h1 .white-text")
    assert element_section_where_to_h1.text == 'OpenWeather'

    element_section_where_to_h2 = driver.find_element(By.CSS_SELECTOR, ".mobile-padding h2 .black-text")
    assert element_section_where_to_h2.text == 'Weather forecasts, nowcasts and history in a fast and elegant way'

    driver.get('https://openweathermap.org/')
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'


@pytest.mark.parametrize('city', cities)
def test_fill_search_city_field(driver, city):
    driver.get('https://openweathermap.org/')
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
    driver.get('https://openweathermap.org/')
    wait = WebDriverWait(driver, 15)
    wait.until_not(EC.presence_of_element_located(load_div))
    search_city_input = driver.find_element(*search_city_field)
    search_city_input.send_keys(city)
    driver.find_element(*search_button).click()
    options = driver.find_elements(*search_dropdown)
    for option in options:
        assert city in option.text


@pytest.fixture()
def open_and_load_page(driver, wait):
    driver.get(URL)
    wait.until_not(EC.presence_of_element_located(load_div))


@pytest.fixture()
def wait(driver):
    wait = WebDriverWait(driver, 25)
    yield wait


def test_should_go_to_sign_in_page(driver, open_and_load_page, wait):
    sign_link = wait.until(EC.presence_of_element_located(sign_in_link))
    driver.execute_script("arguments[0].click();", sign_link)
    assert "sign_in" in driver.current_url, f"\nWrong URL - {driver.current_url}"


def test_should_be_valid_title_on_price_page(driver, open_and_load_page, wait):
    element = driver.find_element(*pricing_link)
    action_chains = ActionChains(driver)
    action_chains.move_to_element(element)
    driver.execute_script("arguments[0].click();", element)
    pricing_text = driver.find_element(*price_page_title).text
    assert pricing_text == "Pricing"


def test_should_be_valid_text_in_sign_in_tab(driver, open_and_load_page, wait):
    driver.find_element(*accept_cookies).click()
    expected_text = 'Sign in'
    element = driver.find_element(*sign_in_link)
    sign_in_text = driver.execute_script("return arguments[0].textContent", element)
    assert sign_in_text == expected_text

