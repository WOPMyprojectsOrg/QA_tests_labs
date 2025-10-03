#write test for add function
def test_task01():
    from tasks.task01 import add
    assert add(2, 3) == 5
    assert add(0, 0) == 0
