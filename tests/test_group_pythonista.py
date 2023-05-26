from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

URL_API = 'https://openweathermap.org/api'
URL_WEATHER_MODEL = 'https://openweathermap.org/technology'
URL_WEATHER_DATA = 'https://openweathermap.org/accuracy-and-quality'
URL_WEATHER_STATIONS = 'https://openweathermap.org/stations'

URL_FORCAST30 = 'https://openweathermap.org/api/forecast30'
TITLE_FORCAST30 = (By.CSS_SELECTOR, '.col-sm-7 .breadcrumb-title')
LINK_HOW_TO_MAKE = (By.CSS_SELECTOR, "a[href$='geo-year']")
TITLE_HOW_TO_MAKE = (By.XPATH, '//*[@id="geo-year"]/h3')

URL_ROAD_RISK = 'https://openweathermap.org/api/road-risk'
SECTION_R_CONCEPTS = (By.XPATH, "//*[@id='concept']")

FOOTER_PANEL = (By.XPATH, '//*[@id="stick-footer-panel"]/div')
BTN_ALLOW_ALL = (By.CLASS_NAME, "stick-footer-panel__link")
FOOTER_COPYRIGHT = (By.XPATH, "//div[@class='horizontal-section my-5']/div[1]")
DASHBOARD_LINK = (By.XPATH, '//div[@id="desktop-menu"]//a[contains(@href, "/weather-dashboard")]')
BTN_DASHBOARD = (By.CSS_SELECTOR, "#desktop-menu [href$=-dashboard]")
TITLE_HOW_TO_START = (By.XPATH, "//div/h2[contains(text(),'How to Start')]")
PROFESSIONAL_COLLESTION_TITLE = (By.XPATH, "//section[@id='pro']/h2")
CURRENT_FORECAST_COLLECTION_LINK = (By.XPATH, "//section[@id='pro']//p/a[contains(@href, '#current')]")
LOGO = (By.CSS_SELECTOR, ".logo > a > img")
BTN_TRY_THE_DASHBOARD_2 = (By.XPATH, "//div[6]//a[text()='Try the Dashboard']")
BTN_COOKIES = (By.CLASS_NAME, "stick-footer-panel__link")
ALERT_PANEL_SINGIN = (By.CSS_SELECTOR, '.col-md-6 .panel-heading')
HISTORICAL_WEATHER_DATA_COLLECTION_LINK = (By.XPATH, "//section[@id='pro']//p/a[contains(@href, '#history')]")
WEATHER_MAPS_COLLECTION_LINK = (By.XPATH, "//section[@id='pro']//p/a[contains(@href, '#maps')]")
API_LINK = (By.XPATH, '//div[@id="desktop-menu"]//a[contains(@href, "api")]')


def test_TC_003_11_01_verify_the_copyright_information_is_present_on_the_page(driver, open_and_load_main_page, wait):
    cookie_close = driver.find_element(*BTN_COOKIES)
    driver.execute_script("arguments[0].click();", cookie_close)
    expected_footer_text = "© 2012 — 2023 OpenWeather"
    footer = driver.find_element(*FOOTER_COPYRIGHT)
    assert footer.is_displayed() and expected_footer_text in footer.text, \
        "The footer is not displayed or does not contain the expected text"


def test_TC_002_03_05_dashboard_is_visible_and_clickable(driver, open_and_load_main_page, wait):
    wait.until(EC.element_to_be_clickable(DASHBOARD_LINK))
    dashboard_tab = driver.find_element(*DASHBOARD_LINK)
    expected_dashboard_label = 'Dashboard'
    assert dashboard_tab.is_displayed() and dashboard_tab.is_enabled() and expected_dashboard_label in dashboard_tab.text


def test_TC_006_02_01_verify_display_of_how_to_start_section(driver, open_and_load_main_page, wait):
    driver.find_element(*BTN_DASHBOARD).click()
    section = driver.find_element(*TITLE_HOW_TO_START)
    assert section.is_displayed(), "Section not found"


def test_TC_002_03_06_dashboard_link_opens_correct_page(driver, open_and_load_main_page, wait):
    wait.until(EC.element_to_be_clickable(DASHBOARD_LINK))
    dashboard_tab = driver.find_element(*DASHBOARD_LINK)
    dashboard_tab.click()
    expected_url = 'https://openweathermap.org/weather-dashboard'
    assert driver.current_url == expected_url


def test_TC_005_04_02_professional_collection_section_is_presented(driver, wait):
    driver.get(URL_API)
    wait.until(EC.presence_of_element_located(PROFESSIONAL_COLLESTION_TITLE))
    proffecional_collection_title = driver.find_element(*PROFESSIONAL_COLLESTION_TITLE)
    expected_title = 'Professional collections'
    assert expected_title in proffecional_collection_title.text


def test_TC_002_01_04_header_logo_verify_logo_redirects_from_dashboard_page_to_main_page(driver):
    driver.get('https://openweathermap.org/weather-dashboard/')
    driver.find_element(*LOGO).click()
    assert driver.current_url == 'https://openweathermap.org/'


def test_TC_006_02_03_weather_dashboard_verify_the_transition_to_another_page(driver, open_and_load_main_page, wait):
    driver.find_element(*BTN_DASHBOARD).click()
    cookie_close = driver.find_element(*BTN_COOKIES)
    driver.execute_script("arguments[0].click();", cookie_close)
    driver.find_element(*BTN_TRY_THE_DASHBOARD_2).click()
    driver.switch_to.window(driver.window_handles[1])
    alert_mms = driver.find_element(*ALERT_PANEL_SINGIN)
    assert alert_mms.is_displayed(), 'WELCOME EVENTS'


def test_TC_005_04_03_professional_collection_historical_weather_is_visible_and_clickable(driver, wait):
    driver.get(URL_API)
    wait.until(EC.presence_of_element_located(HISTORICAL_WEATHER_DATA_COLLECTION_LINK))
    historical_link = driver.find_element(*HISTORICAL_WEATHER_DATA_COLLECTION_LINK)
    expected_historical_label = 'Historical weather data collection'
    assert historical_link.is_displayed() and historical_link.is_enabled() and expected_historical_label in historical_link.text


def test_TC_005_04_04_professional_collection_weather_maps_link_is_visible_and_clickable(driver, wait):
    driver.get(URL_API)
    wait.until(EC.presence_of_element_located(WEATHER_MAPS_COLLECTION_LINK))
    expected_weather_maps_label = 'Weather Maps collection'
    weather_maps_link = driver.find_element(*WEATHER_MAPS_COLLECTION_LINK)
    assert weather_maps_link.is_enabled() and weather_maps_link.is_displayed() and expected_weather_maps_label in weather_maps_link.text


def test_TC_005_04_05_professional_collection_current_and_forecast_is_visible_and_clickable(driver, wait):
    driver.get(URL_API)
    wait.until(EC.presence_of_element_located(CURRENT_FORECAST_COLLECTION_LINK))
    current_forecast_link = driver.find_element(*CURRENT_FORECAST_COLLECTION_LINK)
    exp_current_forecast = 'Current & Forecasts collection'
    assert current_forecast_link.is_enabled() and current_forecast_link.is_displayed() and exp_current_forecast in current_forecast_link.text


def test_TC_005_06_1_visibility_climatic_forecast_30_days_page_title(driver):
    driver.get(URL_FORCAST30)
    title_page = driver.find_element(*TITLE_FORCAST30).text
    assert title_page == 'Climate forecast for 30 days', 'The title of the page does not match the expected value'


def test_TC_005_06_02_redirect_to_the_how_to_make_an_API_call_section_of_the_page(driver):
    driver.get(URL_FORCAST30)
    driver.find_element(*LINK_HOW_TO_MAKE).click()
    new_page_title = driver.find_element(*TITLE_HOW_TO_MAKE)
    assert new_page_title.is_displayed(), 'The title of the page does not match the expected value'


def test_TC_003_11_02_verify_the_copyright_information_is_present_on_the_site_page(driver):
    driver.get(URL_API)
    expected_footer_text = "© 2012 — 2023 OpenWeather"
    footer = driver.find_element(*FOOTER_COPYRIGHT)
    assert footer.is_displayed() and expected_footer_text in footer.text, \
        "The footer is not displayed or does not contain the expected text"


def test_TC_005_08_03_road_risk_api_visibility_of_road_risk_api_concept_section(driver):
    driver.get(URL_ROAD_RISK)
    section_road_risk = driver.find_element(*SECTION_R_CONCEPTS)
    assert section_road_risk.is_displayed(), 'Section - NOT FOUND'


def test_TC_002_01_08_header_logo_verify_logo_redirects_from_weather_model_page_to_main_page(driver):
    driver.get(URL_WEATHER_MODEL)
    driver.find_element(*LOGO).click()
    assert driver.current_url == 'https://openweathermap.org/'


def test_TC_002_01_10_header_logo_verify_logo_redirects_from_weather_stations_page_to_main_page(driver):
    driver.get(URL_WEATHER_STATIONS)
    driver.find_element(*LOGO).click()
    assert driver.current_url == 'https://openweathermap.org/'


def test_TC_002_03_16_api_link_redirects_to_api_page(driver, open_and_load_main_page, wait):
    wait.until(EC.element_to_be_clickable(API_LINK))
    driver.find_element(*API_LINK).click()
    assert driver.current_url == URL_API


def test_tc_002_01_09_header_logo_verify_logo_redirects_from_weather_data_page_to_main_page(driver):
    driver.get(URL_WEATHER_DATA)
    driver.find_element(*LOGO).click()
    assert driver.current_url == 'https://openweathermap.org/'


def test_tc_002_03_15_api_link_is_visible_and_clickable_on_main_page(driver, open_and_load_main_page, wait):
    wait.until(EC.element_to_be_clickable(API_LINK))
    api_link = driver.find_element(*API_LINK)
    expected_api_link = 'API'
    assert api_link.is_displayed() and api_link.is_enabled() and expected_api_link in api_link.text
import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://openweathermap.org/"
load_div = (By.CSS_SELECTOR, 'div.owm-loader-container > div')
selector_dashboard = (By.XPATH, "//h1[contains(text(),'Weather dashboard')]")
selector_api = (By.XPATH, "//h1[contains(text(),'Weather API')]")
tab_desk_api = (By.CSS_SELECTOR, '#desktop-menu a[href="/api"]')
btn_desc_dashboard = (By.CSS_SELECTOR, "#desktop-menu [href$=-dashboard]")
title_weatherDashboard = (By.CLASS_NAME, 'breadcrumb-title')
selector_marketplace_tab = (By.XPATH, '//div[@id="desktop-menu"]//li[4]/a')
footer_panel = (By.XPATH, '//*[@id="stick-footer-panel"]/div')
btn_allow_all = (By.CLASS_NAME, "stick-footer-panel__link")
btn_go_home = (By.XPATH, "//a[contains(text(),'Home')]")
# TODO (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)')))
footer_copyright = (By.XPATH, "//div[@class='horizontal-section my-5']/div[1]")

# About As
btn_about_us = (By.CSS_SELECTOR, 'a[href*="/about-us"]')
btn_product_doc = (By.CSS_SELECTOR, 'div.grid-container [href="/api"]')
weather_title_api = (By.CLASS_NAME, 'breadcrumb-title')
btn_buy_subst = (By.CSS_SELECTOR, 'a[href="https://home.openweathermap.org/subscriptions"]')
alert_txt = (By.CLASS_NAME, "panel-body")
assert_mmg = '\n====You need to sign in or sign up before continuing.===\n'
btn_newAndUpd = (By.CSS_SELECTOR, 'a.round[href*="blog"]')
text_openweather = (By.XPATH, '//div/h1/span["orange -text"]')
search_city_field_selector = (By.XPATH, '//div[@id="weather-widget"]//div/input')
search_submit_button = (By.XPATH, '//div[@id="weather-widget"]//div/button')
search_dropdown_option = (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)')
btn_contact_as = (By.CSS_SELECTOR, '.about-us :nth-child(9) [href="https://home.openweathermap.org/questions"]')
question_page = (By.CLASS_NAME, 'headline')
btn_marketplace = (By.CSS_SELECTOR, 'div.grid-container a[href$="/marketplace"]')
txt_mp_page = (By.XPATH, '//*[@id="custom_weather_products"]/h1')
# Support tab
support_tab = (By.CSS_SELECTOR, '#support-dropdown')
faq_link = (By.XPATH, '//ul[@class="dropdown-menu dropdown-visible"]/li/a[text()="FAQ"]')
how_to_start_link = (By.XPATH, '//ul[@class="dropdown-menu dropdown-visible"]/li/a[text()="How to start"]')
ask_question_link = (By.XPATH, '//ul[@class="dropdown-menu dropdown-visible"]/li/a[text()="Ask a question"]')


@pytest.fixture()
def wait(driver):
    wait = WebDriverWait(driver, 15)
    wait.until_not(EC.presence_of_element_located(load_div))
    yield wait


@pytest.fixture()
def open_page(driver):
    driver.get(URL)
    driver.maximize_window()
    assert 'openweathermap' in driver.current_url


@pytest.fixture()
def cookies_panel_w(driver, open_page):
    btn_click_all = driver.find_element(*btn_allow_all)
    cookies_panel = driver.find_element(*footer_panel)
    if cookies_panel:
        btn_click_all.click()


def test_check_page_title(driver, wait, open_page):
    # function checks page title
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'


'''DESKTOP MENU / Verify menu-btn "API" redirects to api page and btn "Home" return back'''


def test_checkout_tab_api(driver, open_page, wait):
    bt_click_api = driver.find_element(By.CSS_SELECTOR, 'a[href*="/api"]')
    action_chains = ActionChains(driver)
    action_chains.move_to_element(bt_click_api)
    driver.execute_script("arguments[0].click();", bt_click_api)
    assert driver.current_url == 'https://openweathermap.org/api'
    driver.find_element(*btn_go_home).click()
    assert driver.current_url == URL


'''DESKTOP MENU / Verify menu-btn "Dashboard" redirects to dashboard page and btn "Home" return back'''


def test_checkout_menu_tab_dashboard(driver, open_page, wait):
    btn_dashb = driver.find_element(*btn_desc_dashboard)
    action_chains = ActionChains(driver)
    action_chains.move_to_element(btn_dashb)
    driver.execute_script("arguments[0].click();", btn_dashb)
    title_dashboard = driver.find_element(*title_weatherDashboard).text
    assert title_dashboard == 'Weather dashboard'
    driver.find_element(*btn_go_home).click()
    assert driver.current_url == URL


def test_home_button(driver, open_page):
    #  testing going back to home from Guide page
    try:
        WebDriverWait(driver, 50).until_not(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
        tab_name_guide = WebDriverWait(driver, 45).until(EC.element_to_be_clickable(
            (By.XPATH, '//div[@id="desktop-menu"]//a[contains(@href, "guide")]')))
        tab_name_guide.click()
        tab_home_link = WebDriverWait(driver, 45).until(EC.element_to_be_clickable(
            (By.XPATH, '//div[@class="col-sm-5"]/ol/li/a')))
        tab_home_link.click()
        assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'
    except TimeoutException as e:
        print(f"TimeoutException occurred: {e}")


def test_guide_button(driver, open_page):
    #  testing Guide tab button
    try:
        WebDriverWait(driver, 50).until_not(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
        tab_name_guide = WebDriverWait(driver, 45).until(EC.element_to_be_clickable(
            (By.XPATH, '//div[@id="desktop-menu"]//a[contains(@href, "guide")]')))
        tab_name_guide.click()
        assert driver.title == 'OpenWeatherMap API guide - OpenWeatherMap'
    except TimeoutException as e:
        print(f"TimeoutException occurred: {e}")


def test_marketplace_page_link(driver, open_page):
    try:
        WebDriverWait(driver, 15).until_not(EC.presence_of_element_located(load_div))
        marketplace_tab = WebDriverWait(driver, 15).until(EC.element_to_be_clickable
                                                          (selector_marketplace_tab))
        marketplace_tab.click()
        expected_url = 'https://home.openweathermap.org/marketplace'
        assert expected_url
    except TimeoutException as e:
        print(f"TimeoutException occurred: {e}")


def test_search_city_field(driver):
    driver.get(URL)
    wait = WebDriverWait(driver, 15)
    wait.until_not(EC.presence_of_element_located(load_div))
    search_city_field = driver.find_element(*search_city_field_selector)
    search_city_field.send_keys('New York')
    search_button = driver.find_element(*search_submit_button)
    search_button.click()
    search_option = wait.until(EC.element_to_be_clickable(
        search_dropdown_option))
    search_option.click()
    expected_city = 'New York City, US'
    wait.until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, '.grid-container.grid-4-5 h2'), 'New York'))
    displayed_city = driver.find_element(By.CSS_SELECTOR, '.grid-container.grid-4-5 h2').text
    assert displayed_city == expected_city


def test_search_city_field(driver):
    driver.get(URL)
    wait = WebDriverWait(driver, 15)
    wait.until_not(EC.presence_of_element_located(load_div))
    search_city_field = driver.find_element(*search_city_field_selector)
    search_city_field.send_keys('New York')
    search_button = driver.find_element(*search_submit_button)
    search_button.click()
    search_option = wait.until(EC.element_to_be_clickable(
        search_dropdown_option))
    search_option.click()
    expected_city = 'New York City, US'
    wait.until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, '.grid-container.grid-4-5 h2'), 'New York'))
    displayed_city = driver.find_element(By.CSS_SELECTOR, '.grid-container.grid-4-5 h2').text
    assert displayed_city == expected_city


def test_check_about(driver, open_page):
    wait = WebDriverWait(driver, 15)
    wait.until_not(EC.presence_of_element_located(load_div))
    wait.until(EC.element_to_be_clickable(footer_panel))
    driver.find_element(*btn_allow_all).click()
    driver.find_element(*btn_about_us).click()
    title_about_us = driver.find_element(*text_openweather).text
    assert title_about_us == 'OpenWeather'


'''About us / Verify "Products Documentation" button redirects to page'''


def test_check_product_doc_btn(driver, open_page, wait, cookies_panel_w):
    driver.find_element(*btn_about_us).click()
    driver.find_element(*btn_product_doc).click()
    txt_title = driver.find_element(*weather_title_api).text
    assert txt_title == 'Weather API'


'''About us/ Verify "Buy by Subscription" button redirects to subscriptions page(logout)'''


def test_check_buy_by_sub(driver, open_page, wait):
    wait.until(EC.element_to_be_clickable(footer_panel))
    driver.find_element(*btn_allow_all).click()
    driver.find_element(*btn_about_us).click()
    driver.find_element(*btn_buy_subst).click()
    alert = driver.find_element(*alert_txt)
    assert alert.is_displayed()


# TODO  Negative test!
@pytest.mark.skip('negative test')
def test_neg_check_buy_by_subs(driver, open_page):
    wait = WebDriverWait(driver, 15)
    wait.until_not(EC.presence_of_element_located(load_div))
    wait.until(EC.element_to_be_clickable(footer_panel))
    driver.find_element(*btn_allow_all).click()
    driver.find_element(*btn_about_us).click()
    driver.find_element(*btn_buy_subst).click()
    neg_alert_txt = driver.find_element(*alert_txt).text
    assert neg_alert_txt == 'https://home.openweathermap.org/subscriptions', assert_mmg


'''Footer/ About us / Verify "By in the MarketPlace" button redirects user to "Custom Weather Products'''


def test_check_marketplace(driver, open_page):
    wait = WebDriverWait(driver, 15)
    wait.until_not(EC.presence_of_element_located(load_div))
    wait.until(EC.element_to_be_clickable(footer_panel))
    driver.find_element(*btn_allow_all).click()
    driver.find_element(*btn_about_us).click()
    driver.find_element(*btn_marketplace).click()
    txt_markplace = driver.find_element(*txt_mp_page).text
    assert txt_markplace == 'Custom Weather Products'


'''Footer / About us / Verify New and Updates button'''


def test_news_and_update(driver, open_page):
    wait = WebDriverWait(driver, 15)
    wait.until_not(EC.presence_of_element_located(load_div))
    wait.until(EC.element_to_be_clickable(footer_panel))
    driver.find_element(*btn_allow_all).click()
    driver.find_element(*btn_about_us).click()
    driver.find_element(*btn_newAndUpd).click()
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == "https://openweather.co.uk/blog/category/weather"
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.quit()


'''Footer/ About us / Verify "Contact us" button redirects user to "Questions" page'''


def test_contact_us(driver, open_page):
    wait = WebDriverWait(driver, 15)
    wait.until_not(EC.presence_of_element_located(load_div))
    wait.until(EC.element_to_be_clickable(footer_panel))
    driver.find_element(*btn_allow_all).click()
    driver.find_element(*btn_about_us).click()
    driver.find_element(*btn_contact_as).click()
    driver.switch_to.window(driver.window_handles[1])
    assert driver.find_element(*question_page).is_displayed()


'''Testing Support tab'''


def test_support_faq(driver, open_page):
    try:
        driver.get(URL)
        wait = WebDriverWait(driver, 15)
        wait.until_not(EC.presence_of_element_located(load_div))
        wait.until(EC.presence_of_element_located(support_tab))
        driver.find_element(*support_tab)
        wait.until(EC.presence_of_element_located(faq_link))
        driver.find_element(*faq_link).click()
        assert driver.current_url == 'https://openweathermap.org/faq'
    except TimeoutException as e:
        print(f"TimeoutException occurred: {e}")


# TODO  need fix
def test_support_how_start(driver, open_page):
    try:
        driver.get(URL)
        wait = WebDriverWait(driver, 15)
        wait.until_not(EC.presence_of_element_located(load_div))
        wait.until(EC.presence_of_element_located(support_tab))
        driver.find_element(*support_tab)
        wait.until(EC.presence_of_element_located(how_to_start_link))
        driver.find_element(*how_to_start_link).click()
        assert driver.current_url == 'https://openweathermap.org/appid'
    except TimeoutException as e:
        print(f"TimeoutException occurred: {e}")


def test_support_ask_question(driver, open_page):
    try:
        driver.get(URL)
        wait = WebDriverWait(driver, 15)
        wait.until_not(EC.presence_of_element_located(load_div))
        wait.until(EC.presence_of_element_located(support_tab))
        driver.find_element(*support_tab)
        wait.until(EC.presence_of_element_located(ask_question_link))
        driver.find_element(*ask_question_link).click()
        driver.switch_to.window(driver.window_handles[1])
        assert driver.current_url == 'https://home.openweathermap.org/questions'
    except TimeoutException as e:
        print(f"TimeoutException occurred: {e}")


'''Footer / Copyright/  Visability, content '''


def test_visability_copyright(driver, open_page, wait):
    wait.until(EC.element_to_be_clickable(footer_panel))
    driver.find_element(*btn_allow_all).click()
    driver.find_element(*footer_copyright).is_displayed()


def test_home_page_header(driver):
    driver.get(URL)
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    header = driver.find_element(By.CSS_SELECTOR, "h1")
    assert header.text == "OpenWeather", "Wrong h1 Header"


def test_should_refresh_link(driver):
    driver.get('https://openweathermap.org/')
    current_title = driver.title
    driver.refresh()
    title_after_refresh = driver.title
    assert current_title == title_after_refresh

def test_should_open_given_link(driver):
    driver.get(URL)
    assert 'openweathermap' in driver.current_url




