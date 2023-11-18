from src.funcs import get_payment_type


def test_get_payment_type():
    payment_type = get_payment_type("Счет 59956820797131895975")
    assert payment_type == "Счет **5975"
    payment_type = get_payment_type("Visa Classic 6831982476737658")
    assert payment_type == "Visa Classic 6831 98** ****7658"


#def test_parse():
#    operation = parse_file(file)
#    assert isinstance(operation, list)