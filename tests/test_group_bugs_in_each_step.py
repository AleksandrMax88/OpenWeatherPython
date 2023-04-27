from selenium.webdriver.common.by import By
URL = 'https://openweathermap.org/'


def test_should_open_given_link(driver):
    driver.get(URL)
    assert 'openweathermap' in driver.current_url


def test_check_page_title(driver):
    driver.get(URL)
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'
    print(f'The site title is: {driver.title}')


def test_look_for_buttons(driver):
    driver.get(URL)
    search_button = driver.find_element(By.CSS_SELECTOR, "button[class='button-round dark']")
    weather_widget_weather_button = driver.find_element(By.XPATH, "//*[contains(text(),'Different Weather')]")
    weather_widget_metric_button = driver.find_element(By.XPATH, "//*[contains(text(),'Metric')]")
    weather_widget_imperial_button = driver.find_element(By.XPATH, "//*[contains(text(),'Imperial')]")
    expected_button1 = 'Search'
    expected_button2 = 'Different Weather?'
    expected_button3 = 'Metric: °C, m/s'
    expected_button4 = 'Imperial: °F, mph'
    assert search_button.text == expected_button1
    assert weather_widget_weather_button.text == expected_button2
    assert weather_widget_metric_button.text == expected_button3
    assert weather_widget_imperial_button.text == expected_button4
    print('\n')
    print(f'The Search button text is: {search_button.text}')
    print(f'The Weather button text is: {weather_widget_weather_button.text}')
    print(f'The Metric button text is: {weather_widget_metric_button.text}')
    print(f'The Imperial button text is: {weather_widget_imperial_button.text}')


