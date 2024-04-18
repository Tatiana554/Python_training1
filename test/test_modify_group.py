# Тест для модификации группы

from model.group import Group  # импортирвание класса из другой папки group


def test_modify_group_name(app):
    old_groups = app.group.get_group_list()
    group = Group(name="New group")
    # ↓ вспомогательный метод для модифткации группы
    app.group.modify_first_group(group)
    # запоминание (сохранение)id т.к в измененной группе id уже есть
    group.id = old_groups [0].id
    new_groups = app.group.get_group_list()  # новый список групп
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    # сравнение новогосписка групп со страым списком
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_modify_group_header(app):
 #   old_groups = app.group.get_group_list()
  #  # ↓ вспомогательный метод для модифткации группы
   # app.group.modify_first_group(Group(header="New header"))
    #new_groups = app.group.get_group_list()  # новый список групп
    #assert len(old_groups) == len(new_groups)

