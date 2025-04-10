from main.app import summ, delete

def test_summ():
    result = summ(2, 5)
    assert 7 == result


def test_delete():
    result = delete(6, 2)
    assert 3 != result