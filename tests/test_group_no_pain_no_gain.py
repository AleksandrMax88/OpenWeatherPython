from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

logo_locator = (By.CSS_SELECTOR, ".logo > a > img")
ASK_A_QUESTION_LINK = (By.XPATH, "(//*[contains(text(),'question')])[3]")
allow_all_cookies_locator = (By.XPATH, '//*[contains(text(), "Allow all")]')
PARTNERS_LINK = (By.CSS_SELECTOR, '#desktop-menu a[href="/examples"]')
PARTNERS_PAGE_TITLE = (By.XPATH, '//h1')
WEATHER_MAP = (By.CSS_SELECTOR, 'a[href="/api#maps"]')


def test_TC_002_01_01_return_from_guide_page_to_main_page_by_clicking_on_logo(driver):
    driver.get('https://openweathermap.org/guide')
    driver.find_element(*logo_locator).click()
    assert driver.current_url == 'https://openweathermap.org/'


def test_TC_003_08_02_ask_a_question_link_is_visible(driver, open_and_load_main_page, wait):
    element = wait.until(EC.visibility_of_element_located(ASK_A_QUESTION_LINK))
    assert element.is_displayed(), "Ask a question link is not visible in the footer"


def test_TC_003_13_03_verify_visibility_and_clickability_of_allow_all_button(driver, open_and_load_main_page, wait):
    element = driver.find_element(*allow_all_cookies_locator)
    wait.until(EC.element_to_be_clickable(allow_all_cookies_locator))
    assert element.is_displayed() and element.is_enabled()


def test_TC_002_03_21_partners_link_leads_to_correct_page(driver, open_and_load_main_page):
    driver.find_element(*PARTNERS_LINK).click()
    partners_title_text = driver.find_element(*PARTNERS_PAGE_TITLE).text
    assert partners_title_text == "Partners and solutions"


def test_TC_003_03_09_weather_map_link_in_footer_to_be_clickable(driver, open_and_load_main_page, wait):
    element = driver.find_element(*WEATHER_MAP)
    wait.until(EC.element_to_be_clickable(WEATHER_MAP))
    assert element.is_enabled()


def test_TC_003_12_05_ask_a_question_link_leads_to_correct_page(driver, open_and_load_main_page):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.find_element(*ASK_A_QUESTION_LINK).click()
    window_question_page = driver.window_handles[1]
    driver.switch_to.window(window_question_page)
    assert driver.current_url == "https://home.openweathermap.org/questions"


def test_TC_002_03_22_partners_link_is_visible_and_clickable(driver, open_and_load_main_page, wait):
    element = wait.until(EC.visibility_of_element_located(PARTNERS_LINK))
    assert element.is_displayed() and element.is_enabled(), '"Partners" link is not visible or clickable'


def test_TC_003_08_03_ask_a_question_link_is_clickable(driver,open_and_load_main_page, wait):
    element = driver.find_element(*ASK_A_QUESTION_LINK)
    wait.until(EC.element_to_be_clickable(ASK_A_QUESTION_LINK))
    assert element.is_enabled(), "Ask a question link is not clickable"
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://openweathermap.org/'
WRONG_LOGIN = 'error@gmail.com'
WRONG_PASSWORD = 'error'
SIGN_IN_PAGE = 'https://home.openweathermap.org/users/sign_in'

def test_should_open_given_link(driver):
    driver.get(URL)
    assert 'openweathermap' in driver.current_url

def test_check_page_title(driver):
    driver.get(URL)
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'

def test_check_logo_visibility(driver):
    driver.get(URL)
    logo = driver.find_element(By.CSS_SELECTOR, "#first-level-nav > li.logo > a > img")
    assert logo.is_displayed() == True

def test_wrong_login_password(driver):
    driver.get(SIGN_IN_PAGE)
    element = driver.find_element(By.XPATH, "//div[@class='input-group']//input[@id='user_email']")
    text = element.get_attribute('placeholder')
    assert text == 'Enter email'
    element.send_keys(WRONG_LOGIN)
    element = driver.find_element(By.XPATH, "//div[@class='input-group']//input[@id='user_password']")
    text = element.get_attribute('placeholder')
    assert text == 'Password'
    element.send_keys(WRONG_PASSWORD)
    cssValue = driver.find_element(By.XPATH, "//input[@value='Submit']").value_of_css_property(
        "cursor"
    )
    assert cssValue == "pointer"
    driver.find_element(By.XPATH, "//input[@value='Submit']").click()
    driver.find_element(By.XPATH, "//div[@class='panel-heading']"), 'NO ALERT'
    driver.find_element(By.XPATH, "//*[contains(text(), 'Invalid Email or password.')]")

def test_fill_search_city_field(driver):
    driver.get('https://openweathermap.org/')
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    search_city_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search city']")
    search_city_field.send_keys('New York')
    search_button = driver.find_element(By.CSS_SELECTOR, "button[class ='button-round dark']")
    search_button.click()
    search_option = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)')))
    search_option.click()
    expected_city = 'New York City, US'
    WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, '.grid-container.grid-4-5 h2'), 'New York'))
    displayed_city = driver.find_element(By.CSS_SELECTOR, '.grid-container.grid-4-5 h2').text
    assert displayed_city == expected_city


def test_recover_password(driver):
    driver.get(SIGN_IN_PAGE)
    cssValue = driver.find_element(By.XPATH, "//a[@href='#']").value_of_css_property(
        "cursor"
    )
    assert cssValue == "pointer"
    driver.find_element(By.XPATH, "//a[@href='#']").click()
    element = driver.find_element(By.XPATH, "//input[@class='form-control string email optional']")
    text = element.get_attribute('placeholder')
    assert text == 'Enter email'
    driver.find_element(By.XPATH, "//input[@class='form-control string email optional']").send_keys(WRONG_LOGIN)
    cssValue = driver.find_element(By.XPATH, "//input[@value='Send']").value_of_css_property(
        "cursor"
    )
    assert cssValue == "pointer"
    WebDriverWait(driver, 10).until_not(EC.text_to_be_present_in_element_value(
        (By.XPATH, "//input[@value='Send']"), "Create user"))
    driver.find_element(By.XPATH, "//input[@value='Send']").click()
    assert "users/password" in driver.current_url
    driver.find_element(By.XPATH, "//div[@class='panel-heading']"), 'NO ERROR MESSAGE!'
    driver.find_element(By.XPATH, "// *[contains(text(), 'Email not found')]"), 'NO EMAIL NOT FOUND MESSAGE!'
    driver.find_element(By.XPATH, "//div[@class='sign-form']"), 'NO FORGOT YOUR PASSWORD FORM!!'
    driver.find_element(By.XPATH, "//*[contains(text(),'Forgot your password?')]")
    element = driver.find_element(By.ID, "user_email")
    text = element.get_attribute('placeholder')
    assert text == 'Enter email'
    element = driver.find_element(By.ID, "user_email")
    text = element.get_attribute('value')
    assert text == WRONG_LOGIN
    driver.find_element(By.XPATH, "//input[@value='Change password']"), 'NO CHANGE PASSWORD BUTTON!'

def test_signin_form_with_empty_fields(driver):
    driver.get('https://home.openweathermap.org/users/sign_in')
    element = driver.find_element(By.XPATH, "//div[@class='input-group']//input[@id='user_email']")
    text = element.get_attribute('placeholder')
    assert text == 'Enter email'
    element = driver.find_element(By.XPATH, "//div[@class='input-group']//input[@id='user_password']")
    text = element.get_attribute('placeholder')
    assert text == 'Password'
    driver.find_element(By.XPATH, "//input[@value='Submit']").click()
