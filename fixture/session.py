# Класс, помощник по работе с сессиями, вспомагательные методы
import ast

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
        wait = WebDriverWait(self.driver, 10)
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
        while len(self.driver.find_elements(By.CSS_SELECTOR,
                                            "form[name='logout'] > a")) > 0:  # пока на странице есть элемент logout, кликать на него
            self.driver.find_element(By.CSS_SELECTOR, "form[name='logout'] > a").click()




