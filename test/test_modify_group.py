# Тест для модификации группы

from model.group import Group  # импортирвание класса из другой папки group


def test_modify_group_name(app):
    old_groups = app.group.get_group_list()
    # ↓ вспомогательный метод для модифткации группы
    app.group.modify_first_group(Group(name="New group"))
    new_groups = app.group.get_group_list()  # новый список групп
    assert len(old_groups) == len(new_groups)


def test_modify_group_header(app):
    old_groups = app.group.get_group_list()
    # ↓ вспомогательный метод для модифткации группы
    app.group.modify_first_group(Group(header="New header"))
    new_groups = app.group.get_group_list()  # новый список групп
    assert len(old_groups) == len(new_groups)

