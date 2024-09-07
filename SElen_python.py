# вебдрайвер-это программа, которая управляет браузером
# для кадого вебраузера свой драйвер
# импортируем из селениум вебдрайвер
from selenium import webdriver
# импорт класса  Ву для работы с селекторами
from selenium.webdriver.common.by import By
# импортируем время-чтобы программа могла подождать, когда страница откроется и тд
import time
# импортируем пайтест
# import pytest

# создаем функцию теста--путем прописания конструкции def test_имя функции
def test_pytotrg():
    # добавление опций к драйверу
    options = webdriver.ChromeOptions()
    # добавляем аргумент открытия в режиме инкогнито
    options.add_argument('--incognito')
    # добавляем откртия окна по размерам
    options.add_argument('--window-size=1920,1080')
    # иницивлизация драйвера с добавлением опций
    browser = webdriver.Chrome(options=options)
    # адрес сайта
    url = 'https://python.org'
    # дравер включает неявное ожидание-пока не появится какой-нибудь элемент на странице
    browser.implicitly_wait(5)
    # переход на сайт
    browser.get(url)
    # ожидание драйвера
    time.sleep(5)
    # поиск элемента
    element = browser.find_element(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[2]/span/a[3]')
    # используем  метод javascript для прокрутки до элемента на странице
    browser.execute_script('arguments[0].scrollIntoView(true);', element)
    # assert специальная конструкция, позволяющая проверять предположения о значениях произвольных данных
    # в произвольном месте программы. В данном случае-ожидание того, что текст будет совпадать. Именно это и будет проверять тест
    assert element.text=='PyQt'
    # закрытие браузера
    time.sleep(10)
