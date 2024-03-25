# класс, вспомагательные методы которые относятся к работе с группами в addbook
from selenium.webdriver.common.by import By

class GroupHelper:

    def __init__ (self, app): # конструктор. Вкачетсве парамметра принимает ссылку на Application (app - фикстура)
        self.app = app

    def return_to_groups_page(self):
        # возврат на страницу со списком групп
        self.driver = self.app.driver
        self.driver.find_element(By.LINK_TEXT, "group page").click()

    def create(self, group):  # group это сгруппированый параметр который передается из другой папки (класса) group
        # он позволяет не прописывать каждый параметр, потомучто все параметры прописаны внутри него (в папке)
        # создание новой группы
        self.driver = self.app.driver  # доступ к драйверу, потомучто в Application есть конструктор для запука драйвера ???
        self.open_groups_page()
        self.driver.find_element(By.NAME, "new").click()
        # открытие формы и её заполнение
        self.driver.find_element(By.NAME, "group_name").click()
        # ↓ name (в (group.name)) название параметра (созданый через refactor→parameter),этот пармаетр входит в метод create_group
        # явные значения параметров передаются в сгруппированом методе, а здесь были убраны дефолтные знаения через refactor→change signature
        # дальше group (в ((group.name) это свойства объекта из класса Group (из папки group)
        self.driver.find_element(By.NAME, "group_name").send_keys(group.name)
        self.driver.find_element(By.NAME, "group_header").click()
        self.driver.find_element(By.NAME, "group_header").send_keys(group.header)
        self.driver.find_element(By.NAME, "group_footer").click()
        self.driver.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # создание группы (сохранение)
        self.driver.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()

    def open_groups_page(self):
        # открывается страница с гуппами
        self.driver.find_element(By.LINK_TEXT, "groups").click()


    def delete_first_group(self):
        self.driver = self.app.driver  # доступ к драйверу, потомучто в Application есть конструктор для запука драйвера ???
        self.open_groups_page()
        # select first group   выбрать первую группу
        self.driver.find_element(By.NAME, "selected[]").click()
        # submit deletion      удалить группу
        self.driver.find_element(By.NAME, "delete").click()
        self.return_to_groups_page() # возврат на страницу с группами, как на фронте