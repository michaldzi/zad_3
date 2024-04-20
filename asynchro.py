from multiprocessing import Process
import logging
import time


logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)


def factorize_list(number):
    start_time = time.time()

    factors = []
    for i in range(1, number + 1):

        if number % i == 0:
            factors.append(i)

    end_time = time.time()
    execution_time = end_time - start_time
    logger.debug(f"wynik {factors}")
    logger.debug(f"Czas wykonania: {execution_time} sekundy")
    return factors


if __name__ == "__main__":
    input_list = [128, 255, 99999, 10651060]
    processes = []
    for i in input_list:
        processes = []
        pr1 = Process(target=factorize_list, args=(i,))
        pr1.start()
        processes.append(pr1)
        logger.debug(processes)
