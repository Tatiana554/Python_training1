
def test_delete_first_group(app): # это объект созданый фикстурой
    # ↓ в методе передаются явные значения параметров username и password
    # эти параметры были созданы в несгруппированных методах, конкретно в login
    # добавляется app т.к. эты функция  обращается к функции application
    app.session.login(username ="admin",password ="secret")
    # ↑ добавлен session потомучто функция раскрыта в помощнике session
    # Создание объекта типа Group ↓ ( в скобках это параметры объекта передаваемые в его конструктор в папке group)
    # и поскольку объект Group в отдельном файле group, вначале этого файла делается импорт
    app.group.delete_first_group()
    app.session.logout()

