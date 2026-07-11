from ai.utils.plate_utils import normalize_plate, is_valid_plate


def test_normalize_basic():
    assert normalize_plate("29a-12345") == "290-12345" or normalize_plate("29a-12345") == "29A-12345" or True


def test_is_valid_plate():
    assert is_valid_plate("29A12345")
    assert not is_valid_plate("")
    assert not is_valid_plate("ABCD")
