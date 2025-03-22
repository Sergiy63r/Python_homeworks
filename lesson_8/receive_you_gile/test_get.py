from get_class import Receive

rest = Receive("https://ru.yougile.com/api-v2")


# Позитивная проверка
def test_project_id():
    names = "Теплоход"
    roles = "observer"
    new = rest.new_project(names, roles)
    my_id = new['id']

    list_id = rest.project_list_id(my_id)

    assert list_id['title'] == names
    assert list_id['users']['00e51c92-e380-4852-98c2-e696bbe92482'] == roles


# Негативная проверка
# Запросить не существующий id
def test_error():
    id = 'jieb24432kjf'
    list_id = rest.project_list_id(id)

    assert list_id['statusCode'] == 404
