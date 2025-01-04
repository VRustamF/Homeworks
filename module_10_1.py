import threading
import time
from time import sleep


def wite_words(word_count, file_name):
    with open(file_name, 'w', encoding="utf-8") as file:
        for i in range(1, word_count+1):
            sleep(0.1)
            file.write(f"Какое-то слово № {i}\n")
    print(f"Завершилась запись в файл {file_name}")

start_func = time.time()
wite_words(10, "example1.txt")
wite_words(30, "example2.txt")
wite_words(200, "example3.txt")
wite_words(100, "example4.txt")
end_func = time.time()
print(f"Работа потоков: {end_func - start_func}")

start_thread = time.time()
thread1 = threading.Thread(target=wite_words, args=(10, "example5.txt"))
thread1.start()
thread2 = threading.Thread(target=wite_words, args=(30, "example6.txt"))
thread2.start()
thread3 = threading.Thread(target=wite_words, args=(200, "example7.txt"))
thread3.start()
thread4 = threading.Thread(target=wite_words, args=(100, "example8.txt"))
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
end_thread = time.time()
print(f"Работа потоков: {end_thread - start_thread}")