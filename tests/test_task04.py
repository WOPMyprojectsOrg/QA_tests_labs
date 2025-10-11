# Напишите тесты для функции max_of_three(a, b, c)
def test_max_of_three():
    from tasks.task04 import max_of_three()
    assert max_of_three(-1, -2, -3) == -1
    assert max_of_three(0, 1, 20) == 20