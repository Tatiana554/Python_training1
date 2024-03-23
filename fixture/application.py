from selenium import webdriver # импорт для запуска конструктов (Вебдрайвера) Apllication ↓
from selenium.webdriver.common.by import By  # импорт к классу By дает поиск элементов по различным критериям
from fixture.session import SessionHelper # импорт помощника


class Application:

   def __init__ (self): # конструктор для запуски браузера
        self.driver = webdriver.Firefox()  # запускайется драйвер, т.е браузер
        self.session = SessionHelper(self)  # в помощник передается ссылка на фикстуру и в этой фикстуре есть функция запуска вебдрайвера
        # ↑ т.е. помощник получает ссылку на объект класса Application, это дает возможность в будущем , в одном помощнике обратится к другому помощнику
        # через объект класса Application
        self.vars = {}


# ↓ НЕ СГРУППИРОВАННЫЕ (развернутые,вспомагаьельные) методы сценария, в каждом методе отдельно расписаны шаги (почему они в обрятном порядке хз)

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

   def open_home_page(self):
         # открытие главной страницы
       self.driver.get("http://localhost/addressbook/")
   # self позволяет вызвать метод который был создан через refactor

   def destroy (self): # метод для закрытия браузера
       self.driver.quit()
