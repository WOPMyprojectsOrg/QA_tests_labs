# Напишите тесты для функции primes_up_to(n)
def test_task06():
    from tasks.task06 import primes_up_to
    assert primes_up_to(3)==[1,2,3]
    assert primes_up_to(5)==[1,2,3,5]
    assert primes_up_to(10)==[1,2,3,5,7]