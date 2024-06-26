from selenium import webdriver  # импорт для запуска конструктов (Вебдрайвера) Apllication ↓
from selenium.webdriver.common.by import By  # импорт к классу By дает поиск элементов по различным критериям
from fixture.session import SessionHelper  # импорт помощника
from fixture.group import GroupHelper  # импорт класса GroupHelper из папки group/fixture в нем все вспомагательные методы которые относятся к работе с группами в addbook


class Application:

    def __init__(self):  # конструктор для запуски браузера
        self.session = SessionHelper(self)  # в помощник передается ссылка на фикстуру и в этой фикстуре есть функция запуска вебдрайвера
        # ↑ т.е. помощник получает ссылку на объект класса Application, это дает возможность в будущем , в одном помощнике обратится к другому помощнику
        # через объект класса Application
        self.driver = webdriver.Firefox()  # запускайется драйвер,браузер
        self.group = GroupHelper(self)  # ссылка на класс GroupHelper из папки group/fixture в нем все вспомагательные методы которые относятся к работе с группами в addbook
        self.vars = {}


# Блок перехвата исключений
    def is_valid(self):  # метод ля проверки работы браузера, если браузер упадет
        try:
            self.driver.current_url  # запрос у браузера какой текущий адрес открытой страницы
            return True
        except:  # если возникли проблемы то возвращается ошибка
             return False

    # ↓ НЕ СГРУППИРОВАННЫЕ (развернутые,вспомагаьельные) методы сценария, в каждом методе отдельно расписаны шаги
    def open_home_page(self):
        # открытие главной страницы
        self.driver.get("http://localhost/addressbook/")


    # self позволяет вызвать метод который был создан через refactor

    def destroy(self):  # метод для закрытия браузера, разрушает фикстуру
        self.driver.quit()
