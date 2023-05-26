
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest

URL = 'https://openweathermap.org/'
BUTTON_PRICING = (By.XPATH, '//div[@id="desktop-menu"]//a[text()="Pricing"]')
DISPLAYED_TITLE = (By.CSS_SELECTOR, 'h1.breadcrumb-title')
FIELD_WEATHER_IN_YUOR_CITY = (By.CSS_SELECTOR, "#desktop-menu input[placeholder='Weather in your city']")
ALERT_NOTIFICATION = (By.CSS_SELECTOR, "#forecast_list_ul .alert.alert-warning")
STRING_ENTERED_CITY = (By.CSS_SELECTOR, "#search_str")
SEARCH_DROPDOWN_OPTION = (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)')
SEARCH_DROPDOWN_MENU = By.CLASS_NAME, 'search-dropdown-menu'
SEARCH_CITY_FIELD = (By.CSS_SELECTOR, "input[placeholder='Search city']")
SEARCH_BUTTON = (By.CSS_SELECTOR, "button[class ='button-round dark']")
DISPLAYED_CITY = (By.CSS_SELECTOR, '.grid-container.grid-4-5 h2')
BUTTON_GUIDE = (By.XPATH, "//div[@id='desktop-menu']//a[text()='Guide']")
BUTTON_INITIATIVES = (By.XPATH, '//*[@id="mobile-menu"]/li[8]/a')
DISPLAYED_TITLE_INITIATIVE = (By.CSS_SELECTOR, 'h1.breadcrumb-title')
MENU_INITIATIVE = "arguments[0].click();"
BUTTON_GET_ACCESS = (By.XPATH, '//a[text()="Get access"]')
DISPLAYED_AUTHORISATION_WINDOW = (By.XPATH, '//h3[text()="Sign In To Your Account"]')
BUTTON_MAPS = (By.CSS_SELECTOR, '#desktop-menu ul li:nth-child(6) a')
BUTTON_LEARN_MORE = "//div[2]/div/div/div[2]/div/div[1]/center/a"
chart_weather = (By.XPATH, "//*[@id='chart-component']")
FOOTER_WEBSITE = (By.XPATH, '//*[@id="footer-website"]')
GOOGLE_PLAY_LINK = (By.XPATH, '//*[@id="footer-website"]/div/div[3]/div/a[2]/img')
METRIC_SWITCH = (By.XPATH, "//div[@class='switch-container']/div[contains(text(), 'Metric')]")

NOTIFICATION_PANE = (By.ID, 'forecast_list_ul')
NOTIFICATION_BUTTON = (By.CSS_SELECTOR, '.alert.alert-warning a.close')

BUTTON_SUPPORT = (By.XPATH, "//*[@id='support-dropdown']")
BUTTON_FAQ = (By.XPATH, "//*[@id='support-dropdown-menu']//a[@href='/faq']")
BUTTON_HOW_TO_START = (By.XPATH, "//*[@id='support-dropdown-menu']//a[@href='/appid']")
BUTTON_ASK_A_QUESTION = (By.XPATH, "//*[@id='support-dropdown-menu']//a[@href='https://home.openweathermap.org/questions']")
DISPLAYED_TITLE_ASK_A_QUESTION = (By.CSS_SELECTOR, "h4.headline")
MENU_DASHBOARD = (By.CSS_SELECTOR, '#desktop-menu ul li:nth-child(3)')
IMAGE = (By.XPATH, "//*[@class='responsive']")
MENU_INITIATIVES = (By.XPATH, '//*[@id="mobile-menu"]/li[8]/a')
logo_locator = (By.XPATH, '//*[@class="logo"]/a/img')
title_locator = (By.XPATH, '//p[text()="Product Collections"]')
URLs = ['https://openweathermap.org/',
        'https://openweathermap.org/guide',
        'https://openweathermap.org/api',
        'https://openweathermap.org/weather-dashboard',
        'https://openweathermap.org/price',
        'https://openweathermap.org/our-initiatives',
        'https://openweathermap.org/examples',
        'https://home.openweathermap.org/users/sign_in',
        'https://openweathermap.org/faq',
        'https://openweathermap.org/appid',
        'https://home.openweathermap.org/questions']

widget_constructor_URL = 'https://openweathermap.org/widgets-constructor'
maps_URL = 'https://openweathermap.org/weathermap'
student_initiative_URL = 'https://openweathermap.org/our-initiatives/student-initiative'

title_free_data_for_students = (By.XPATH, "//span[text()='Free Data for Students']")
dashboard_URL = 'https://openweathermap.org/weather-dashboard'

metric_toggle = (By.XPATH, '//span[@id="metric"]')
imperial_units = (By.XPATH, '//span[text()="°F"]')
metric_units = (By.XPATH, '//span[text()="°C"]')
pricing_URL = 'https://openweathermap.org/price'
button_detailed_pricing_locators = [(By.XPATH, '//*[@id="current"]//a[2]'),
                                    (By.XPATH, '//*[@id="history"]//a[2]')]
widgets_locators = [(By.XPATH, '//*[@id="container-openweathermap-widget-11"]'),
                    (By.XPATH, '//*[@id="container-openweathermap-widget-12"]'),
                    (By.XPATH, '//*[@id="container-openweathermap-widget-13"]'),
                    (By.XPATH, '//*[@id="container-openweathermap-widget-14"]'),
                    (By.XPATH, '//*[@id="container-openweathermap-widget-15"]'),
                    (By.XPATH, '//*[@id="container-openweathermap-widget-16"]'),
                    (By.XPATH, '//*[@id="container-openweathermap-widget-17"]'),
                    (By.XPATH, '//*[@id="container-openweathermap-widget-18"]'),
                    (By.XPATH, '//*[@id="container-openweathermap-widget-19"]')]

result_locator = (By.XPATH, '//a[contains(@href, "city")]')
search_field_locator = (By.XPATH, '//*[@placeholder="Weather in your city"]')
condition_URL = 'https://openweathermap.org/weather-conditions'
thunderstorm_locator = (By.XPATH, '//a[contains(@href, "#Thunderstorm")]/ancestor-or-self::table//tr')
clouds_locator = (By.XPATH, '//a[contains(@href, "#Clouds")]/ancestor-or-self::table')
pricing_plans_locators = [(By.XPATH, '//h4[text()="Free"]'),
                          (By.XPATH, '//h4[text()="Startup"]'),
                          (By.XPATH, '//h4[text()="Developer"]'),
                          (By.XPATH, '//h4[text()="Professional"]'),
                          (By.XPATH, '//h4[text()="Enterprise"]')]

def test_TC_002_03_08_open_pricing(driver, open_and_load_main_page):
    button_pricing = driver.find_element(*BUTTON_PRICING)
import time
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import datetime
from selenium.webdriver import ActionChains


test_email = 'chosenonex1@gmail.com'
test_password = 'gNrts5W?K_.qLFu'
API_key = '2c254a2efb0b9008ce295e94a0939a2f'
cities = ['Moscow', 'Paris']


URL = 'https://openweathermap.org/'

def test_open_page(driver):
    driver.get(URL)
    assert 'openweathermap' in driver.current_url # проверка наличия строки в url

def test_sing_in_empty_fields(driver):
    driver.get('https://home.openweathermap.org/users/sign_in')
    driver.find_element(By.XPATH, '//*[@id="new_user"]/input[3]').click()
    alert = driver.find_element(By.XPATH, '//*[@class="panel-body"]')
    assert alert.text == 'Invalid Email or password.'

def test_sing_in_positive(driver):
    driver.get('https://home.openweathermap.org/users/sign_in')
    email_form = driver.find_element(By.XPATH, '//*[@id = "user_email"]')
    email_form.click()
    email_form.send_keys(test_email)
    password_form = driver.find_element(By.XPATH, '//*[@id = "user_password"]')
    password_form.click()
    password_form.send_keys(test_password)
    remember_checkbox = driver.find_element(By.XPATH, '//*[@id = "user_remember_me"]')
    assert remember_checkbox.is_selected() == False
    driver.find_element(By.XPATH, '//*[@id="new_user"]/input[3]').click()
    driver.implicitly_wait(15)
    assert 'home.openweathermap' in driver.current_url
    alert = driver.find_element(By.XPATH, '//*[@class="panel-body"]')
    assert alert.text == 'Signed in successfully.'

def test_open_weather_map(driver):
    driver.get(URL)
    WebDriverWait(driver, 15).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    # driver.implicitly_wait(15)
    # zoom_map = WebDriverWait(driver, 15).until(
    #     EC.presence_of_element_located((By.XPATH, '//a[contains(@href, "weathermap?zoom")]')))
    driver.find_element(By.XPATH, '//button[text()="Allow all"]').click()
    zoom_map = driver.find_element(By.XPATH, '//a[contains(@href, "weathermap?zoom")]')
    zoom_map.click()
    window_weathermap_zoom = driver.window_handles[1] # возвращаем дескриптор новой страницы
    driver.switch_to.window(window_weathermap_zoom) # переключаем selenium на новую страницу
    assert driver.title == 'Interactive weather maps - OpenWeatherMap'

@pytest.mark.parametrize('city', cities)
def test_current_weather_api(city):
    payload = {'q': f'{city}',
               'appid': f'{API_key}'}
    response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=payload)
    response_data = response.json()
    assert response.status_code == 200
    expected_keys = ['coord', 'weather', 'main', 'id', 'name']
    for key in expected_keys:
        assert key in response_data.keys()
    assert response.json()['name'] == city


def test_fahrenheit_click(driver):
    driver.get('https://openweathermap.org/')
    driver.maximize_window()
    temp_change = driver.find_element(By.XPATH, '//*[@id="weather-widget"]/div[1]/div/div/div[1]/div[2]')
    WebDriverWait(driver, 15).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    ActionChains(driver).drag_and_drop_by_offset(temp_change, 72, 0).perform()
    far_temp = driver.find_element(By.XPATH, '//*[@id="weather-widget"]/div[2]/div[1]/div[1]/div[2]/div[1]/span').text
    assert far_temp.find("F") != -1 # проверяем, что в элементе на сайте с температурой есть буква F - фаренгейт

def test_8_days_forecast(driver): # проверка, что отображается прогноз на 8 дней
    driver.get("https://openweathermap.org/")
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    amount_of_days = len(driver.find_elements(By.XPATH, '//*[@class="day-list"]/li'))
    assert amount_of_days == 8

def test_check_title(driver):
    driver.get(URL)
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    weekly_weather = driver.find_element(By.CSS_SELECTOR, '.daily-container.block.mobile-padding h3')
    title_weekly_weather = weekly_weather.text
    assert title_weekly_weather =='8-day forecast'

def test_notification_tab_singIN(driver):
    driver.get("https://home.openweathermap.org/users/sign_in")
    assert driver.title == 'Members'
    user_email = driver.find_element(By.XPATH, "//input[@class='string email optional form-control']")
    user_email.send_keys('marina@mail.ru')
    user_password = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    user_password.send_keys('marina111')
    driver.find_element(By.XPATH, "//input[@value='Submit']").click()
    notification_title = driver.find_element(By.CSS_SELECTOR, ".panel-heading")
    disp_title = notification_title.text
    assert disp_title == 'Alert'
    notification_content = driver.find_element(By.CSS_SELECTOR, ".panel-body")
    disp_text = notification_content.text
    assert disp_text == 'Invalid Email or password.'


def test_title_site(driver):
    driver.get(URL)
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    title = driver.find_element(By.XPATH, "//h1")
    assert title.text == "OpenWeather"



def test_open_pricing(driver):
    driver.get("https://openweathermap.org/")
    button_pricing = driver.find_element(By.XPATH, '//div[@id="desktop-menu"]//a[text()="Pricing"]')
    action_chains = ActionChains(driver)
    action_chains.move_to_element(button_pricing)
    driver.execute_script("arguments[0].click();", button_pricing)
    expected_title = "Pricing"
<<<<<<< HEAD
    displayed_title = driver.find_element(*DISPLAYED_TITLE).text
    assert displayed_title == expected_title

def test_TC_002_02_03_verify_result_of_search_for_invalid_city_name(driver, open_and_load_main_page, wait):
    search_weather_in_your_city = driver.find_element(*FIELD_WEATHER_IN_YUOR_CITY)
    entered_invalid_city_name = "LJKJJ"
    search_weather_in_your_city.send_keys(entered_invalid_city_name)
    actions = ActionChains(driver)
    actions.send_keys(Keys.ENTER).perform()
    wait.until(EC.presence_of_element_located(ALERT_NOTIFICATION))
    displayed_notification = driver.find_element(*ALERT_NOTIFICATION)
    notification = displayed_notification.text
    assert notification == "×\nNot found"

def test_TC_002_02_04_verify_displaying_entered_city_name_in_Search_field(driver, open_and_load_main_page, wait):
    search_weather_in_your_city = driver.find_element(*FIELD_WEATHER_IN_YUOR_CITY)
    entered_city_name = "LJKJJ"
    search_weather_in_your_city.send_keys(entered_city_name)
    actions = ActionChains(driver)
    actions.send_keys(Keys.ENTER).perform()
    wait.until(EC.presence_of_element_located(ALERT_NOTIFICATION) )
    search_result_city_name = driver.find_element(*STRING_ENTERED_CITY)
    found_city = search_result_city_name.get_property("value")
    assert found_city == entered_city_name

@pytest.mark.parametrize('URL', URLs)
def test_TC_002_01_03_Logo_is_visible(driver, wait, URL):
    driver.get(URL)
    logo = driver.find_element(*logo_locator)
    assert logo.is_displayed(), "Logo is not visible"

def test_TC_001_01_02_2_fill_city_field_in_cirillic(driver, open_and_load_main_page, wait):
    search_city_input = driver.find_element(*SEARCH_CITY_FIELD)
    search_city_input.send_keys('Кишинев')
    driver.find_element(*SEARCH_BUTTON).click()
    wait.until(EC.element_to_be_clickable(SEARCH_DROPDOWN_OPTION)).click()
    expected_city = 'Chisinau, MD'
    wait.until(EC.text_to_be_present_in_element(DISPLAYED_CITY, 'Chisinau'))
    actual_city = driver.find_element(*DISPLAYED_CITY)
    assert expected_city == actual_city.text

def test_TC_001_09_06_switched_on_Fahrenheit(driver):
    driver.get(widget_constructor_URL)
    toggle_position = driver.find_element(*metric_toggle)
    expected_position = 'color: rgb(235, 110, 75);'
    if toggle_position.get_attribute("style") == expected_position:
        toggle_position.click()
        for widget_locator in widgets_locators:
            WebDriverWait(driver, 15).until(EC.visibility_of_element_located(widget_locator))
        imperial_units_number = driver.find_elements(*imperial_units)
        assert len(imperial_units_number) == 14
    else:
        imperial_units_number = driver.find_elements(imperial_units)
        assert len(imperial_units_number) == 14

@pytest.mark.parametrize('URL', URLs)
def test_TC_003_03_01_Product_Collections_title_is_visible(driver, URL):
    driver.get(URL)
    module_title = driver.find_element(*title_locator)
    assert module_title.is_displayed(), "Product Collections title is not visible"

def test_TC_002_02_01_search_result_contains_city(driver, open_and_load_main_page, wait):
    search = driver.find_element(*search_field_locator)
    search.click()
    search.send_keys('Bangkok')
    search.send_keys(Keys.ENTER)
    driver.implicitly_wait(15)
    cities = driver.find_elements(*result_locator)
    for city in cities:
        assert 'Bangkok' in city.text

def test_TC_001_12_01_thunderstorm_group_contains_items(driver):
    driver.get(condition_URL)
    codes_number = driver.find_elements(*thunderstorm_locator)
    assert len(codes_number) >= 3

def test_TC_002_03_03_01_open_guide(driver, open_and_load_main_page):
    button_guide = driver.find_element(*BUTTON_GUIDE)
    action_chains = ActionChains(driver)
    action_chains.move_to_element(button_guide)
    driver.execute_script("arguments[0].click();", button_guide)
    expected_title = "Guide"
    displayed_title = driver.find_element(*DISPLAYED_TITLE).text
    assert displayed_title == expected_title

def test_TC_002_01_06_Verify_return_to_Main_page_from_Interactive_weather_maps(driver):
    driver.get(maps_URL)
    driver.find_element(*logo_locator).click()
    assert driver.current_url == 'https://openweathermap.org/'

def test_TC_010_01_04_check_open_page_our_initiative(driver, open_and_load_main_page):
    button_initiatives = driver.find_element(*BUTTON_INITIATIVES)
    action_chains = ActionChains(driver)
    action_chains.move_to_element(button_initiatives)
    driver.execute_script(MENU_INITIATIVE, button_initiatives)
    expected_title = "Our Initiatives"
    displayed_title = driver.find_element(*DISPLAYED_TITLE_INITIATIVE).text
    assert displayed_title == expected_title

def test_TC_010_02_05_Get_access_open_authorization_window(driver, open_and_load_main_page):
    driver.get(student_initiative_URL)
    button_get_access = driver.find_element(*BUTTON_GET_ACCESS)
    action_chains = ActionChains(driver)
    action_chains.move_to_element(button_get_access)
    driver.execute_script("arguments[0].click();", button_get_access)
    expected_title = 'Sign In To Your Account'
    displayed_title = driver.find_element(*DISPLAYED_AUTHORISATION_WINDOW).text
    assert displayed_title == expected_title

def test_TC_002_03_12_open_maps(driver, open_and_load_main_page):
    driver.find_element(*BUTTON_MAPS).click()
    assert '/weathermap' in driver.current_url

def test_TC_002_03_03_09_open_faq(driver, open_and_load_main_page):
    button_support = driver.find_element(*BUTTON_SUPPORT)
    action_chains = ActionChains(driver)
    action_chains.move_to_element(button_support)
    driver.execute_script("arguments[0].click();", button_support)
    button_faq = driver.find_element(*BUTTON_FAQ)
    action_chains.move_to_element(button_faq)
    driver.execute_script("arguments[0].click();", button_faq)
    expected_title = "Frequently Asked Questions"
    displayed_title = driver.find_element(*DISPLAYED_TITLE).text
    assert displayed_title == expected_title

def test_TC_006_01_05_image_on_dashboard(driver, open_and_load_main_page, wait):
    driver.find_element(*MENU_DASHBOARD).click()
    wait.until(EC.element_to_be_clickable(MENU_DASHBOARD))
    image = driver.find_element(*IMAGE)
    assert image.is_displayed(), "Image is not visible"

def test_TC_001_12_05_Clouds_group_of_codes_visible(driver):
    driver.get(condition_URL)
    clouds_codes = driver.find_element(*clouds_locator)
    assert clouds_codes.is_displayed()

def test_TC_006_04_04_pricing_plans_are_visible(driver):
    driver.get(dashboard_URL)
    for plan_locator in pricing_plans_locators:
        plan = driver.find_element(*plan_locator)
        assert plan.is_displayed()

def test_TC_002_03_03_11_open_ask_a_question(driver, open_and_load_main_page):
    button_support = driver.find_element(*BUTTON_SUPPORT)
    action_chains = ActionChains(driver)
    action_chains.move_to_element(button_support)
    driver.execute_script("arguments[0].click();", button_support)
    window_before = driver.window_handles[0]
    button_ask_a_question = driver.find_element(*BUTTON_ASK_A_QUESTION)
    action_chains.move_to_element(button_ask_a_question)
    driver.execute_script("arguments[0].click();", button_ask_a_question)
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    expected_title = "Ask a question"
    displayed_title = driver.find_element(*DISPLAYED_TITLE_ASK_A_QUESTION).text
    assert displayed_title == expected_title

def test_TC_002_02_06_verify_closing_of_NotFound_notification(driver, open_and_load_main_page, wait):
    search_weather_in_your_city = driver.find_element(*FIELD_WEATHER_IN_YUOR_CITY)
    entered_invalid_city_name = "LJKJJ"
    search_weather_in_your_city.send_keys(entered_invalid_city_name)
    actions = ActionChains(driver)
    actions.send_keys(Keys.ENTER).perform()
    wait.until(EC.presence_of_element_located(ALERT_NOTIFICATION))
    close_not = driver.find_element(*NOTIFICATION_BUTTON)
    close_not.click()
    pane = driver.find_element(*NOTIFICATION_PANE)
    assert len(pane.get_attribute("innerHTML")) == 0


def test_TC_002_03_03_10_open_how_to_start(driver, open_and_load_main_page):
    button_support = driver.find_element(*BUTTON_SUPPORT)
    action_chains = ActionChains(driver)
    action_chains.move_to_element(button_support)
    driver.execute_script("arguments[0].click();", button_support)
    button_how_to_start = driver.find_element(*BUTTON_HOW_TO_START)
    action_chains.move_to_element(button_how_to_start)
    driver.execute_script("arguments[0].click();", button_how_to_start)
    expected_title = "How to start using professional collections"
    displayed_title = driver.find_element(*DISPLAYED_TITLE).text
    assert displayed_title == expected_title


def test_TC_001_09_05_switched_on_Celsius(driver):
    driver.get(widget_constructor_URL)
    toggle_position = driver.find_element(*metric_toggle)
    expected_position = 'color: rgb(235, 110, 75);'
    if toggle_position.get_attribute("style") == expected_position:
        action = ActionChains(driver)
        action.double_click(toggle_position).perform()
        for widget_locator in widgets_locators:
            WebDriverWait(driver, 15).until(EC.visibility_of_element_located(widget_locator))
        metric_units_number = driver.find_elements(*metric_units)
        assert len(metric_units_number) == 14
    else:
        driver.find_element(*metric_toggle).click()
        for widget_locator in widgets_locators:
            WebDriverWait(driver, 15).until(EC.visibility_of_element_located(widget_locator))
        metric_units_number = driver.find_elements(metric_units)
        assert len(metric_units_number) == 14
        

def test_TC_001_08_03_chart_current_weather(driver, open_and_load_main_page, wait):
    chart_present = wait.until(EC.visibility_of_element_located(chart_weather))
    assert chart_present
        

def test_TC_010_01_01_1_check_button_learn_more(driver, open_and_load_main_page):
    menu_initiatives = driver.find_element(*MENU_INITIATIVES)
    action_chains = ActionChains(driver)
    action_chains.move_to_element(menu_initiatives)
    driver.execute_script("arguments[0].click();", menu_initiatives)
    actual_button = driver.find_element(By.XPATH, BUTTON_LEARN_MORE)
    expected_text_on_button = "Learn more"
    assert actual_button.text == expected_text_on_button
        
        
def test_TC_010_02_02_check_free_data_for_students(driver, open_and_load_main_page):
    # 3 redirection in 1 test
    menu_initiatives = driver.find_element(*MENU_INITIATIVES)
    action_chains = ActionChains(driver)
    action_chains.move_to_element(menu_initiatives)
    driver.execute_script("arguments[0].click();", menu_initiatives)
    button_learn = driver.find_element(By.XPATH, BUTTON_LEARN_MORE)
    driver.execute_script("arguments[0].click();", button_learn)
    expected_title = "Free Data for Students"
    actual_title = driver.find_element(*title_free_data_for_students)
    assert expected_title == actual_title.text

        
def test_TC_008_03_01_button_detailing_pricing(driver):
    driver.get(pricing_URL)
    for button_locator in button_detailed_pricing_locators:
        button_p = driver.find_element(*button_locator)
        assert button_p.is_displayed() 


def test_TC_003_12_11_link_Google_Play_leads_to_correct_page_in_GP(driver, open_and_load_main_page, wait):
    driver.execute_script("window.scrollTo(100,document.body.scrollHeight);")
    google_play = driver.find_element(*GOOGLE_PLAY_LINK)
    action_chains = ActionChains(driver)
    action_chains.move_to_element(google_play)
    driver.execute_script("arguments[0].click();", google_play)
    driver.switch_to.window(driver.window_handles[1])
    expected_title = 'OpenWeather'
    # displayed_title = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]//div//h1/span').text
    assert '/play.google' in driver.current_url and expected_title in driver.title

def test_TC_001_01_08_dropdown_list_contain_city_temperature_celsius(driver, open_and_load_main_page, wait):
    metric_button = wait.until(EC.element_to_be_clickable(METRIC_SWITCH))
    assert metric_button.is_displayed() and metric_button.is_enabled()
    search_city_input = driver.find_element(*SEARCH_CITY_FIELD)
    search_city_input.click()
    search_city_input.send_keys('Saint Petersburg')
    driver.find_element(*SEARCH_BUTTON).click()
    wait.until(EC.element_to_be_clickable(SEARCH_DROPDOWN_MENU))
    dropdown_list = driver.find_element(*SEARCH_DROPDOWN_MENU)
    for city in dropdown_list.find_elements(By.CSS_SELECTOR, 'li'):
        assert '°C' in city.text

=======
    displayed_title = driver.find_element(By.CSS_SELECTOR, 'h1.breadcrumb-title').text
    assert displayed_title == expected_title


def test_current_time(driver): # проверка текущей даты и времени
    driver.get(URL)
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    current_time = datetime.datetime.now().utcnow().strftime("%b %d, %I:%M%p")[:12]
    current_time_from_page_str = driver.find_element(
        By.XPATH, '//div[@id="weather-widget"]//descendant::span[@class="orange-text"]').text
    current_time_from_page_obj = datetime.datetime.strptime(current_time_from_page_str, "%b %d, %I:%M%p").utcnow()
    current_time_from_page_final = current_time_from_page_obj.strftime("%b %d, %I:%M%p")[:12]
    assert current_time == current_time_from_page_final
>>>>>>> origin/test



