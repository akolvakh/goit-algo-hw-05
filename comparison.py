import search_boyer_moore as bms
import search_kmp as kmp
import search_rabin_karp as rks
from timeit import timeit

STR_1 = "Розглянемо деякі реалізації відомих алгоритмів пошуку"
STR_2 = "Програмна реалізація досліджених структур даних"

def print_timing(algorithm_name, execution_time, result):
    print(f"{algorithm_name}: {execution_time:.6f} секунд, результат: {result}")

for file in ["Article 1.txt", "Article 2.txt"]:
    with open(file, "r", encoding="windows-1251") as f:
        text = f.read()

        for pattern in [STR_1, STR_2]:
            print(f"\nФайл: {file}, Патерн: {pattern}\n")
            print_timing(
                ">>>БОЄР-МУР",
                timeit("bms.search_boyer_moore(text, pattern)", globals=globals(), number=1),
                bms.search_boyer_moore(text, pattern),
            )
            print_timing(
                ">>>КНУТ-МОРРІС-ПРАТТ",
                timeit("kmp.search_kmp(text, pattern)", globals=globals(), number=1),
                kmp.search_kmp(text, pattern),
            )
            print_timing(
                ">>>РАБІН-КАРП",
                timeit("rks.search_rabin_karp(text, pattern)", globals=globals(), number=1),
                rks.search_rabin_karp(text, pattern),
            )