# класс, вспомагательные методы которые относятся к работе с группами в addbook
from selenium.webdriver.common.by import By


class GroupHelper:

    def __init__(self, app):  # конструктор. Вкачетсве парамметра принимает ссылку на Application (app - фикстура)
        self.app = app

    def open_groups_page(self):
        self.driver = self.app.driver
        # проверка, нужная ли страница открыта
        if not (self.driver.current_url.endswith("/group.php") and len(self.driver.find_elements(By.NAME, "new")) > 0):
            # если урл нужный и найден элемент "new", то:
            # открывается страница с гуппами
            self.driver.find_element(By.LINK_TEXT, "groups").click()

    def create(self, group):  # group это сгруппированый параметр который передается из другой папки (класса) group
        # он позволяет не прописывать каждый параметр, потомучто все параметры прописаны внутри него (в папке)
        # создание новой группы
        self.driver = self.app.driver  # доступ к драйверу, потомучто в Application есть конструктор для запука драйвера ???
        self.open_groups_page()
        self.driver.find_element(By.NAME, "new").click()
        # открытие формы и её заполнение
        self.fill_group_form(group)
        # создание группы (сохранение)
        self.driver.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()

    def change_field_vlue(self, field_name,
                          text):  # метод заполнения поля имя группы, text это произвольное название группы
        self.driver = self.app.driver  # сначала запускается драйвер
        if text is not None:  # если имя группы не пустое то нужно выполнить услвоия ↓
            self.driver.find_element(By.NAME, field_name).click()
            self.driver.find_element(By.NAME, field_name).clear()
            # ↓ name (в (group.name)) название параметра (созданый через refactor→parameter),этот пармаетр входит в метод create_group
            # явные значения параметров передаются в сгруппированом методе, а здесь были убраны дефолтные знаения через refactor→change signature
            # дальше group (в ((group.name) это свойства объекта из класса Group (из папки group)
            self.driver.find_element(By.NAME, field_name).send_keys(text)

    def fill_group_form(self, group):  # метод Заполнения полей группы
        self.driver = self.app.driver  # доступ к драйверу
        self.change_field_vlue("group_name", group.name)
        self.change_field_vlue("group_header", group.header)
        self.change_field_vlue("group_footer", group.footer)

    def select_first_group(self):
        # select first group   выбрать первую группу
        self.driver.find_element(By.NAME, "selected[]").click()

        # Вспомагательный метод Удаления первой  группы

    def delete_first_group(self):
        self.driver = self.app.driver  # доступ к драйверу, потомучто в Application есть конструктор для запука драйвера ???
        self.open_groups_page()
        self.select_first_group()
        # submit deletion      удалить группу
        self.driver.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()  # возврат на страницу с группами, как на фронте

        # Вспомагательный метод Модификация группы

    def modify_first_group(self, new_group_data):
        # ↓ Снаала выполняется переход на страницу со списком групп
        self.driver = self.app.driver  # доступ к драйверу, потомучто в Application есть конструктор для запука драйвера ???
        self.open_groups_page()
        # найти первую группу
        self.select_first_group()
        # ↓ open modification form Открытие формы млдификации
        self.driver.find_element(By.NAME, "edit").click()  # клик на кнопку Edit
        # заполнение формы группы
        self.fill_group_form(new_group_data)
        # подтверждение
        self.driver.find_element(By.NAME, "update").click()
        self.return_to_groups_page()  # возврат на страницу с грцппами

    def return_to_groups_page(self):
        # возврат на страницу со списком групп
        self.driver = self.app.driver
        self.driver.find_element(By.LINK_TEXT, "group page").click()

    # функция для подсчета количства групп на странице
    def count(self):
        self.driver = self.app.driver
        # ↓ отерыть страницу с группами
        self.open_groups_page()
        # len считает длинну списка и ворачивает (return) ее , ↓ поиск чекбоксов (возле групп) с именем selected[]
        return len(self.driver.find_elements(By.NAME, "selected[]"))
