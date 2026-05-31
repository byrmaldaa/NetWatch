from netwatch.core import check_port, dns_lookup


def test_bad_port():
    assert "Порт должен быть числом" in check_port("localhost", "abc")


def test_empty_dns():
    assert "Введите домен" in dns_lookup("")
