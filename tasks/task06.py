# Задача: Напишите функцию, которая возвращает список всех простых чисел до n (включительно).
# Простое число — делится только на 1 и на себя.

def primes_up_to(n):
    primes = [1]
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break         
        if is_prime:
            primes.append(num)
    
    return primes