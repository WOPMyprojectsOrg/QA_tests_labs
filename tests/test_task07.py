# Напишите тесты для функции merge_sorted_lists(a, b)
def test_task07():
    from tasks.task07 import merge_sorted_lists
    assert merge_sorted_lists([1, 3, 5], [2, 4, 6])==[1,2,3,4,5,6]
    assert merge_sorted_lists([0, 3, 5], [-1, 4, 6])==[-1,0,3,4,5,6]
    assert merge_sorted_lists([-10,-5, 0, 1, 3, 5, 10, 12, 14], [2, 4, 6])==[-10, -5, 0, 1, 2, 3 ,4 ,5 ,6 ,10,12,14]