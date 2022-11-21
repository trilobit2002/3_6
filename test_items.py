import time
from selenium.webdriver.common.by import By
# в процедуру передаетя параметр  browser
def test_button_busket_link(browser):
    #Проверяем наличие кнопки "добавить в корзину"
    #assert WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))), "Кнопка 'Добавить в корзину' не найдена"
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(30)
    #assert browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").is_displayed(), 'Кнопка добавления товара в корзину отсутсвует'
    assert browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary"), 'Кнопка добавления товара в корзину отсутсвует'


