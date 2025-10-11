# тест для функции sum_number(n)
def test_sum_number():
    from tasks.task08 import sum_number
    assert sum_number(10) == 23
    assert sum_number(-10) == 0
    assert sum_number(16) == 60