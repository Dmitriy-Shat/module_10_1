from threading import Thread
from datetime import datetime
from time import sleep

time_start = datetime.now()
def write_words(word_count, file_name):
    count = 1
    while count <= word_count:
        with open(file_name, 'a', encoding='utf-8') as file:
            file.write(f'Какое-то слово - {count}\n')
            count += 1
            sleep(0.1)
    return print(f"Завершилась запись в файл {file_name}")

write_1 = write_words(10, 'example1.txt')
write_2 = write_words(30, 'example2.txt')
write_3 = write_words(200, 'example3.txt')
write_4 = write_words(100, 'example4.txt')

time_end_1 = datetime.now()
time_res_1 = time_end_1 - time_start
print(f'Работа функций: {time_res_1}')

thr_5 = Thread(target=write_words, args=(10, 'example5.txt'))
thr_6 = Thread(target=write_words, args=(30, 'example6.txt'))
thr_7 = Thread(target=write_words, args=(200, 'example7.txt'))
thr_8 = Thread(target=write_words, args=(100, 'example8.txt'))

thr_5.start()
thr_6.start()
thr_7.start()
thr_8.start()

thr_5.join()
thr_6.join()
thr_7.join()
thr_8.join()

time_end_2 = datetime.now()
time_res_2 = time_end_2 - time_start - time_res_1
print(f'Работа потоков: {time_res_2}')



