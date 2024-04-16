from model.group import Group # импорт для того что бы класс Группы был виден


def test_delete_first_group(app): # это объект созданый фикстурой
    if app.group.count() == 0: # если нет ни одной группы то:
        # ↓ создать группу
        app.group.create (Group(name = "test"))
    # Удаление объекта типа Group ↓ ( в скобках это параметры объекта передаваемые в его конструктор в папке group)
    # и поскольку объект Group в отдельном файле group, вначале этого файла делается импорт
    app.group.delete_first_group()
    old_groups = app.group.get_group_list()
    new_groups = app.group.get_group_list()  # новый список групп
    assert len(old_groups) == len(new_groups)


