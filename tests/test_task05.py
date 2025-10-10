# Напишите тесты для функции is_palindrome(s)

def test_task05():
    from tasks.task05 import polynom
    assert polynom('A man a plan a canal Panama') == True
    assert polynom('baclajan') == False
    assert polynom(1232432423) == False
    assert polynom(123321) == True
    assert polynom() == True
