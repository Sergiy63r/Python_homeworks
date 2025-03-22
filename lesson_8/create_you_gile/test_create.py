from create_class import Create

rest = Create("https://ru.yougile.com/api-v2")


# Позитивная проверка
def test_new_project():
    names = "КИПиА-2"
    roles = "worker"
    new = rest.new_project(names, roles)

    body = rest.new_project_id()

    assert new['id'] == body['content'][-1]['id']


# Негативная проверка
# Системные роли(roles): worker, admin, observer
# Отправим запрос с несуществующей ролью
def test_error():
    name = "Кофе"
    roles = "user"
    new = rest.new_project(name, roles)

    assert new['statusCode'] == 400
