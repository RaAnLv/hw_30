from main.app import summ

def test_summ():
    result = summ(2, 5)
    assert 7 == result