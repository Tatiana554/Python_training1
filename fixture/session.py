# Класс, помощник по работе с сессиями, вспомагательные методы
import ast
from lib2to3.pgen2 import driver

from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait  # ожидания
from selenium.webdriver.support import expected_conditions as EC


class SessionHelper:

    def __init__(self, app):  # конструктор. В качетсве парамметра принимает ссылку на Application (app - фикстура)
        self.app = app

    def login(self, username, password):
        # логинимся
        self.driver = self.app.driver  # доступ к драйверу, потомучто в Application есть конструктор для запука драйвера ???
        wait = WebDriverWait(self.driver, 5)
        self.app.open_home_page()  # добавлен "app" потомучто  метод open_home_page остается в фикстуре Application
        self.driver.set_window_size(1232, 1043)
        wait.until(EC.element_to_be_clickable((By.NAME, "user"))).click()
        # self.driver.find_element(By.NAME, "user").click()
        # ↓ username название параметра (созданый через refactor→parameter),этот пармаетр входит в метод login
        # явные значения параметров передаются в сгруппированом методе, а здесь были убраны дефолтные знаения через refactor→change signature
        self.driver.find_element(By.NAME, "user").send_keys(username)
        # ↓ password название параметра (созданый через refactor→parameter),этот пармаетр входит в метод login
        # явные значения параметров передаются в сгруппированом методе,а здесь были убраны дефолтные знаения через refactor→change signature
        self.driver.find_element(By.NAME, "pass").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()


    def logout(self):  # логаут
        while len(self.driver.find_elements(By.CSS_SELECTOR, "form[name='logout'] > a")) > 0:  # пока на странице есть элемент logout, кликать на него
            self.driver.find_element(By.CSS_SELECTOR, "form[name='logout'] > a").click()

    def is_logged_in(self):
        self.driver = self.app.driver
        return len(self.driver.find_elements(By.LINK_TEXT, "Logout")) > 0
    # ↑ если на странице есть хотя бы один элемент Логаут

    # проверка имени юзера
    def is_logged_in_as(self, username):
        self.driver = self.app.driver
        return self.driver.find_element(By.XPATH, "//div[@id='top']/form/b").text == f"({username})"

    def ensure_logout(self): # метод для проверки активности сесии юзера, убедится что логаут выполнен
        self.driver = self.app.driver
        if self.is_logged_in(): # если на странице ссылка на логаут, если есть то кликать по ней
            self.logout()

# интелектуальная функция для проверки залогинени пользак или нет
    # если не залогинин то в конец функции , если нет то проверяются условия:
    def ensure_login(self, username, password):
        self.driver = self.app.driver
        if self.is_logged_in(): # если не вошли в систему то проверка :
            if self.is_logged_in_as(username): # если вошли в систему как username, то
                return # делать ничего не нужно, происходит выход из метода
            else: # иначе, если пользак не тот
                self.logout() # выполняется логаут
        self.login(username, password) # выполняется логаут с нужным пользаком
