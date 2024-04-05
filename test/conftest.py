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

fixture = None


@pytest.fixture # метка превращает функцию в инициализатор фикстуры
def app(request):  # эта функция инициализиует фикстуру
    global fixture
    # Метод валидности фикстуры перед каждым тестом
    if fixture is None:
        fixture = Application()  # эта функция будет создаваь фикстуру, то есть объект в Application
    # ↓ в методе передаются явные значения параметров username и password
    # эти параметры были созданы в несгруппированных методах, конкретно в login
    # добавляется fixture т.к. эты функция  обращается к функции application
    # лоинимя для всех тестов
        fixture.session.login(username="admin", password="secret")
    else:
         if not fixture.is_valid():
             fixture = Application()
             fixture.session.login(username="admin", password="secret")
    return fixture  # возвращает фикстуру


''' Закрывающая фикстура, выполняется один раз в конце'''
@pytest.fixture(scope = "session", autouse = True) # autouse  для автоматического выполнения фикстуры, т.к. она явно в методе не прописана
def stop (request):
    # ↓ логаут для всех тестов
    def fin ():
        fixture.session.logout() # добавлен session потомучто функция раскрыта в помощнике session
        fixture.destroy()
    # ↑ добавлен session потомучто функция раскрыта в помощнике session
    request.addfinalizer(fin)  # параметр request c методом addfinalizer (внутри функция для разрушения фикстуы
    # ↑ distroy эта функция которая передается в качестве параметра из папки application
    return fixture  # возвращает фикстуру

# class Testaddgroup(): #  методы  класса Testaddgroup
# метод это функция которая находится внутри класса
# у такой функции всегда должен быть спец параметр self - это объект в котором вызывается метод
# def setup_method(self, method): # функция инициализации, подготовки, она выполняется перед тестовым методом

# self.app = Application () # запуск браузера из метода (из папки)


# def teardown_method(self, method): # функция завершения которая выполняется после тестового метода
# self.app.destroy() # метод для закрытия браузера из функции application