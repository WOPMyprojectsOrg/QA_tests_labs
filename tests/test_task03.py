# Напишите тесты для функции is_even(n)
def test_is_even():
    from test_task03 import is_even
    assert is_even(4) == True
    assert is_even(5) == False
    assert is_even(0) == True