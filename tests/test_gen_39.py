from app.gen_39 import value_39


def test_value_39():
    assert value_39(2) == 2 * 4 + 5
    assert value_39(0) == 5
