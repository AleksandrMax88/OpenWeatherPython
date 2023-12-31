from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import pytest
from selenium.webdriver.support import expected_conditions as EC


footer_website_locator = (By.CLASS_NAME, "inner-footer-container")
company_title_locator = (By.XPATH, "//p[@class='section-heading' and text()='Company']")
company_content_locator = (By.CSS_SELECTOR, ".footer-section > div > p")
gitHub_icon_image = (By.XPATH, "//div[@class='social']//a[6]/img")
logo = (By.CSS_SELECTOR, "#first-level-nav a")
copyright_locator = (By.CSS_SELECTOR, "div.inner-footer-container div.horizontal-section.my-5 span:nth-child(3)")
copyright_expected_result = ['©', '2012 — 2023', 'OpenWeather', '® All rights reserved']
map_info_block = ("css selector", 'a.map-info-block .minutely-section')
URL = 'https://openweathermap.org/'
#The page 'Maps' (/weathermap) doesn't include because it hasn't website footer
PAGES = ['', 'guide', 'api', 'weather-dashboard', 'price', 'our-initiatives', 'examples', 'home/sign_in', 'faq', 'appid']


def test_TC_003_07_01_visibility_of_the_company_module(driver, open_and_load_main_page, wait):
    footer_website = driver.find_element(*footer_website_locator)
    driver.execute_script("arguments[0].scrollIntoView();", footer_website)
    company_title = driver.find_element(*company_title_locator)
    assert company_title.is_displayed()
    content = driver.find_element(*company_content_locator)
    assert content.is_displayed()


def test_TC_003_10_03_visibility_of_GitHub_icon(driver, open_and_load_main_page, wait):
    footer_website = driver.find_element(*footer_website_locator)
    driver.execute_script("arguments[0].scrollIntoView();", footer_website)
    github_icon = driver.find_element(*gitHub_icon_image)
    assert github_icon.is_displayed()


def test_TC_002_01_02_verify_returning_from_API_page_to_main_page_by_clicking_on_logo(driver, wait):
    driver.get('https://openweathermap.org/api')
    driver.find_element(*logo).click()
    assert 'https://openweathermap.org/' in driver.current_url


@pytest.mark.parametrize('page', PAGES)
def test_TC_003_01_01_verify_footer_is_visible_from_all_pages_specified_in_data(driver, wait, page):
    driver.get(f'{URL}{page}')
    footer_website = driver.find_element(*footer_website_locator)
    driver.execute_script('arguments[0].scrollIntoView();', footer_website)
    # print(footer_website.is_displayed(), driver.current_url, driver.title)
    assert footer_website.is_displayed() and driver.title not in 'Page not found (404) - OpenWeatherMap', \
        f'\nFooter is not present on the page - {driver.current_url}'


@pytest.mark.parametrize('page', PAGES)
def test_TC_003_01_02_verify_copyright_is_visible_from_all_pages_specified_in_data(driver, wait, page):
    driver.get(f'{URL}{page}')
    copyright_website = driver.find_element(*copyright_locator)
    driver.execute_script('arguments[0].scrollIntoView();', copyright_website)
    copyright_actual_result = copyright_website.text
    copyright_flag = 1
    for i in copyright_expected_result:
        if i not in copyright_actual_result:
            copyright_flag = 0
    assert copyright_website.is_displayed() and copyright_flag == 1, f'\nCopyright is not present (actual) on the page - {driver.current_url}'

def test_TC_003_10_05_verify_visibility_of_github_icon(driver, open_and_load_main_page):
    github_icon = driver.find_element(*gitHub_icon_image)
    assert github_icon.is_displayed() and github_icon.is_enabled()

def test_TC_001_06_01_redirect_to_interactive_world_weather_map(driver, open_and_load_main_page, wait):
    driver.find_element(*map_info_block).click()
    driver.switch_to.window(driver.window_handles[1])
    wait.until(EC.title_is("Interactive weather maps - OpenWeatherMap"))
    assert driver.title == "Interactive weather maps - OpenWeatherMap"



import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://openweathermap.org/"


def test_check_page_title(driver):
    # function checks page title
    driver.get('https://openweathermap.org')
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'


def test_should_open_given_link(driver):
    driver.get(URL)
    assert 'openweathermap' in driver.current_url


def test_button_search_exist(driver):
    driver.get(URL)
    btn = driver.find_element(By.XPATH, "//button[@type='submit']")
    assert btn.text == "Search"


def test_open_page_map(driver):
    driver.get('https://openweathermap.org/weathermap?basemap=map&cities=true&layer=temperature&lat=30&lon=-20&zoom=5')
    driver.maximize_window()
    assert "weathermap" in driver.current_url