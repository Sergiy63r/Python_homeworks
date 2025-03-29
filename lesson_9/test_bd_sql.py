from sqlalchemy import create_engine
from sqlalchemy.sql import text

db_connection_string = "postgresql://postgres:153@localhost:5432/postgres"    # noqa: E501
db = create_engine(db_connection_string)


def test_users_new():
    rows = text("insert into users(\"user_id\", \"user_email\") values (:us_id, :us_em);")    # noqa: E501
    db.execute(rows, us_id=63163, us_em='sergey58.0@mail.ru')

    db.execute("select * from users where user_id = 63163").fetchall()

    dele = text("delete from  users where user_id = :mf_id")
    db.execute(dele, mf_id=63163)


def test_user_update():
    rows = text("insert into users(\"user_id\", \"user_email\") values (:us_id, :us_em);")    # noqa: E501
    db.execute(rows, us_id=63163, us_em='sergey58.0@mail.ru')

    db.execute("select * from users where user_id = 63163").fetchall()

    ro = text("update users set subject_id = 10 where user_id = 63163")
    db.execute(ro)

    dele = text("delete from  users where user_id = :mf_id")
    db.execute(dele, mf_id=63163)


def test_user_del():
    rows = text("insert into users(\"user_id\", \"user_email\") values (:us_id, :us_em);")    # noqa: E501
    db.execute(rows, us_id=63163, us_em='sergey58.0@mail.ru')

    dele = text("delete from  users where user_id = :mf_id")
    db.execute(dele, mf_id=63163)
