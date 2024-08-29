import pytest
from string_utils import StringUtils

utils = StringUtils()

@pytest.mark.xfail
def test_capitilize():
    #positive
    assert utils.capitilize("slon") == "Slon"
    assert utils.capitilize("vova") == "Vova"

    #negative
    assert utils.capitilize("438") == "error"
    assert utils.capitilize("@#$") == "error"


def test_trim():
    assert utils.trim(" les") == "les"


def test_to_list():
    assert utils.to_list("а,б,в,г") == ["а", "б", "в", "г"]
    assert utils.to_list("хлеб:молоко:сосиски", ":") == ["хлеб", "молоко", "сосиски"]
    assert utils.to_list("1,65,487,25/17") == ["1", "65","487", "25/17"]


def test_contains():
    assert utils.contains("Lada", "L") == True
    assert utils.contains("BmV", "M") == False


def test_delete_symbol():
    assert utils.delete_symbol("Pokemon", "n") == "Pokemo"
    assert utils.delete_symbol("kolObok", "lO") == "kobok"


def test_starts_with():
    assert utils.starts_with("Вертолёт", "В") == True
    assert utils.starts_with("1 метр", "м") == False

    
def test_end_with():
    assert utils.end_with("Час Пик 2", "2") == True
    assert utils.end_with("Tigr", "i") == False


def test_is_empty():
    assert utils.is_empty(" ") == True
    assert utils.is_empty("robot") == False


def test_list_to_string():
    assert utils.list_to_string([7,2,4,5]) == "7, 2, 4, 5"
    assert utils.list_to_string([22,45], ":") =="22:45"
    assert utils.list_to_string(["доски","гвозди","уголки"]) == "доски, гвозди, уголки"
