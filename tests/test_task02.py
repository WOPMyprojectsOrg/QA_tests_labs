# Напишите тесты для функции string_length(s)
def test_task02():
    from tasks.task02 import string_length
    assert string_length("") == 0
    assert string_length("a") == 1
    assert string_length("abcdef") == 6
    assert string_length("abc def") == 7
    assert string_length("@!") == 2