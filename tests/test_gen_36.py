from app.gen_36 import value_36


def test_value_36():
    assert value_36(2) == 2 * 9 + 1
    assert value_36(0) == 1
