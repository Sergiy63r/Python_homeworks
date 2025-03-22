from change_class import Change

rest = Change("https://ru.yougile.com/api-v2")


# Позитивная проверка
def test_new_project():
    names = "КИПиА"
    roles = "worker"
    new = rest.new_project(names, roles)
    my_id = new['id']

    new_name = "КИПиА-2"
    new_role = "worker"
    body = rest.change_project(my_id, new_name, new_role)

    list_pro = rest.project_list()

    assert body['id'] == my_id
    assert list_pro['content'][-1]['title'] == new_name


# Негативная проверка
# Изменить проект с пустым заголовком
def test_error():
    names = "КофеEx"
    roles = "admin"
    new = rest.new_project(names, roles)
    my_id = new['id']

    new_name = ""
    new_role = "worker"
    body = rest.change_project(my_id, new_name, new_role)

    assert body['statusCode'] == 400
