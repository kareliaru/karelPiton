from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def test_pytotrg():
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    options.add_argument('--window-size=1920,1080')
    browser = webdriver.Chrome(options=options)
    url = 'https://python.org'
    browser.implicitly_wait(5)
    browser.get(url)
    time.sleep(5)
    element = browser.find_element(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[2]/span/a[3]')
    browser.execute_script('arguments[0].scrollIntoView(true);', element)
    assert element.text=='PyQt'
    time.sleep(10)
