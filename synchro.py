import time


def factorize(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors


def factorize_list(numbers):
    start_time = time.time()
    result = [factorize(number) for number in numbers]
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time


input_list = [128, 255, 99999, 10651060]
result, execution_time = factorize_list(input_list)
print("Wynik:", result)
print("Czas wykonania:", execution_time, "sekundy")
