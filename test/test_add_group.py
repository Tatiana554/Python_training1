                    # Generated by Selenium IDE
# конструкторы импорт указывают какие используются классы из внешних библиотек ↓
import pytest
import json
from model.group import Group
from fixture.application import Application # импорт класса из папки для запуски браузера
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



  # тестовые МЕТОДЫ ↓ созданные через refactor, они позволяютя сгруппировать и скоратить тестовый сценарий (шаги)
def test_add_group(app): # это объект созданый фикстурой
    # Создание объекта типа Group ↓ ( в скобках это параметры объекта передаваемые в его конструктор в папке group)
    # и поскольку объект Group в отдельном файле group, вначале этого файла делается импорт
    app.group.create(Group(name ="группа 2", header ="444", footer ="555"))

  # ВТОРОЙ СЦЕНАРИЙ (из сгруппированых методов) с пустыми значениями в create_group
def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))





  
