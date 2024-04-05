# Тест для модификации группы

from model.group import Group  # импортирвание класса из другой папки group


def test_modify_group_name(app):
    # ↓ вспомогательный метод для модифткации группы
    app.group.modify_first_group(Group(name="New group"))


def test_modify_group_header(app):
    # ↓ вспомогательный метод для модифткации группы
    app.group.modify_first_group(Group(header="New header"))

