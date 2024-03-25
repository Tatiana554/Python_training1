# Общая фикстура дл всех тестов

# конструкторы импорт указывают какие используются классы из внешних библиотек ↓
import pytest
import json
from model.group import Group # импортирвание класса из другой папки group
from fixture.application import Application # импорт класса из папки для запуски браузера
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

@pytest.fixture (scope = "session") # метка превращает функцию в инициализатор фикстуры
def app(request):  # эта функция инициализиует фикстуру
    fixture = Application()  # эта функция будет создаваь фикстуру, то есть объект в Application
    request.addfinalizer(fixture.destroy)  # параметр request c методом addfinalizer (внутри функция для разрушения фикстуы
    # ↑ distroy эта функция которая передается в качестве параметра из папки application
    return fixture  # возвращает фикстуру

# class Testaddgroup(): #  методы  класса Testaddgroup
# метод это функция которая находится внутри класса
# у такой функции всегда должен быть спец параметр self - это объект в котором вызывается метод
# def setup_method(self, method): # функция инициализации, подготовки, она выполняется перед тестовым методом

# self.app = Application () # запуск браузера из метода (из папки)


# def teardown_method(self, method): # функция завершения которая выполняется после тестового метода
# self.app.destroy() # метод для закрытия браузера из функции application