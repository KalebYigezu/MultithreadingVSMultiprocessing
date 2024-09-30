import time
import threading

def calc_square(numbers):
    print("Calculate square of numbers")
    for n in numbers:
        time.sleep(0.2)
        print("Square : ",n * n)

def calc_cube(numbers):
    print("Calculate cube of numbers")
    for n in numbers:
        time.sleep(0.2)
        print("Cube : ",n * n * n)

arr = [2, 3, 8, 9]

t = time.time()

t1 = threading.Thread(target=calc_square, args=(arr,))
t2 = threading.Thread(target=calc_cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Done in : ",time.time() - t)

---------------------------------------------------------------------------------------------

import time
import multiprocessing

def calc_square(numbers):
    for n in numbers:
        time.sleep(5)
        print('Square ' + str(n * n))

def calc_cube(numbers):
    for n in numbers:
        time.sleep(5)
        print('Cube ' + str(n * n * n))

if __name__ == '__main__':
    arr = [2, 3, 8, 9]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Done")
------------------------------------------------------------------------------------------
import time
import multiprocessing


square_result = []

def calc_square(numbers):
    global square_result
    for n in numbers:
        print('Square ' + str(n * n))
        square_result.append(n * n)
    print("Within a process Result : ", str(square_result))


if __name__ == '__main__':
    arr = [2, 3, 8, 9]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))

    p1.start()
    p1.join()

    print("Not within Result : ",str(square_result))
    print("Done")



''' The main difference between Multithreading and Multiprocess is in the case of Multiprocessing
every process has its own address space. Program variables are not shared between two processes. 
We need to use IPC(interprocess communication techniques) to share data between two processes. '''
