# Класс, помощник по работе с сессиями, вспомагательные методы
from selenium import webdriver
from selenium.webdriver.common.by import By

class SessionHelper:

    def __init__ (self, app): # конструктор. Вкачетсве парамметра принимает ссылку на Application (app - фикстура)
        self.app = app


    def login(self, username, password):
        # логинимся
        self.driver = self.app.driver # доступ к драйверу, потомучто в Application есть конструктор для запука драйвера ???
        self.app.open_home_page() # добавлен "app" потомучто  метод open_home_page остается в фикстуре Application
        self.driver.set_window_size(1232, 1043)
        self.driver.find_element(By.NAME, "user").click()
        # ↓ username название параметра (созданый через refactor→parameter),этот пармаетр входит в метод login
        # явные значения параметров передаются в сгруппированом методе, а здесь были убраны дефолтные знаения через refactor→change signature
        self.driver.find_element(By.NAME, "user").send_keys(username)
        # ↓ password название параметра (созданый через refactor→parameter),этот пармаетр входит в метод login
        # явные значения параметров передаются в сгруппированом методе,а здесь были убраны дефолтные знаения через refactor→change signature
        self.driver.find_element(By.NAME, "pass").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

    def logout(self):  # логаут
        self.driver.find_element(By.LINK_TEXT, "Logout").click()