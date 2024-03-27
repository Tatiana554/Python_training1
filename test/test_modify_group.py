# Тест для модификации группы

from model.group import Group  # импортирвание класса из другой папки group


def test_modify_group_name(app):
    app.session.login(username="admin", password="secret")
    # ↓ вспомогательный метод для модифткации группы
    app.group.modify_first_group(Group(name="New group"))
    app.session.logout()


def test_modify_group_header(app):
    app.session.login(username="admin", password="secret")
    # ↓ вспомогательный метод для модифткации группы
    app.group.modify_first_group(Group(header="New header"))
    app.session.logout()
