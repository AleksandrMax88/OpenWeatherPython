from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

search_city_field_locator = (By.CSS_SELECTOR, "input[placeholder='Search city']")
search_button_locator = (By.CSS_SELECTOR, "button[class='button-round dark']")
search_option_locator = (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)')
displayed_city_locator = (By.CSS_SELECTOR, '.grid-container.grid-4-5 h2')
about_us_locator = (By.XPATH, "//*[text()='About us']")

def testTC_001_01_02_01_displaying_requested_city_name_in_the_search_field(driver, open_and_load_main_page, wait):
    search_city_field = driver.find_element(*search_city_field_locator)
    search_city_field.send_keys('Minsk')
    search_button = driver.find_element(*search_button_locator)
    search_button.click()
    search_option = wait.until(
        EC.element_to_be_clickable((search_option_locator)))
    search_option.click()
    expected_city = 'Minsk, BY'
    wait.until(EC.text_to_be_present_in_element(
        (displayed_city_locator), expected_city))
    displayed_city = driver.find_element(*displayed_city_locator).text
    assert displayed_city == expected_city

def test_TC_003_12_07_about_us_link_leads_to_correct_page(driver, open_and_load_main_page):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.find_element(*about_us_locator).click()
    assert driver.current_url == 'https://openweathermap.org/about-us'

def test_g(driver):
    driver.get('https://openweathermap.org/')
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'


def test_check_website_name(driver):
    driver.get('https://openweathermap.org/')
    website_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'h1 .white-text')))
    assert website_name.text == 'OpenWeather'


def test_check_support_menu(driver):
    driver.get('https://openweathermap.org/')
    WebDriverWait(driver, 10).until_not(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    button_support = driver.find_element(By.CSS_SELECTOR, '#support-dropdown')
    action_chains = ActionChains(driver)
    action_chains.move_to_element(button_support)
    driver.execute_script("arguments[0].click();", button_support)
    assert 'FAQ' and 'How to start' and 'Ask a question' in  driver.page_source




