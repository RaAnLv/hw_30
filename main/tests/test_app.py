from app import delete, func, summ


def test_summ():
    result = summ(2, 5)
    assert 7 == result


def test_delete():
    result = delete(6, 2)
    assert 3 != result


def test_func():
    result = func(2, 1)
    assert 1 == result


def test_summ_2():
    result = summ(2, 2)
    assert 5 != result
