from selenium import webdriver # импорт для запуска конструктов Apllication ↓
from selenium.webdriver.common.by import By  # импорт к классу By дает поиск элементов по различным критериям


class Application:

   def __init__ (self): # конструктор для запуски браузера
        self.driver = webdriver.Firefox()  # запускайется драйвер, т.е браузер
        self.vars = {}



# ↓ НЕ СГРУППИРОВАННЫЕ (развернутые,вспомагаьельные) методы сценария, в каждом методе отдельно расписаны шаги (почему они в обрятном порядке хз)
   def logout(self): # логаут
        self.driver.find_element(By.LINK_TEXT, "Logout").click()

   def return_to_groups_page(self):
        # возврат на страницу со списком групп
       self.driver.find_element(By.LINK_TEXT, "group page").click()

   def create_group(self, group): # group это сгруппированый параметр который передается из другой папки (класса) group
                                # он позволяет не прописывать каждый параметр, потомучто все параметры прописаны внутри него (в папке)
         # создание новой группы
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

   def login(self, username, password):
         # логинимся
       self.open_home_page()
       self.driver.set_window_size(1232, 1043)
       self.driver.find_element(By.NAME, "user").click()
    # ↓ username название параметра (созданый через refactor→parameter),этот пармаетр входит в метод login
    # явные значения параметров передаются в сгруппированом методе, а здесь были убраны дефолтные знаения через refactor→change signature
       self.driver.find_element(By.NAME, "user").send_keys(username)
    # ↓ password название параметра (созданый через refactor→parameter),этот пармаетр входит в метод login
    # явные значения параметров передаются в сгруппированом методе,а здесь были убраны дефолтные знаения через refactor→change signature
       self.driver.find_element(By.NAME, "pass").send_keys(password)
       self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

   def open_home_page(self):
         # открытие главной страницы
       self.driver.get("http://localhost/addressbook/")
   # self позволяет вызвать метод который был создан через refactor

   def destroy (self): # метод для закрытия браузера
       self.driver.quit()
