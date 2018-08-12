import numpy as np
import multiprocessing
import random
import time

def process_func(process_no, result_queue, matA, matB, matA_row):
    result_queue.put('Process' + str(process_no)+ ':' + str(np.matmul(matA[matA_row], matB)))
    #     result[row] = np.matmul(matA[row], matB)
    # print(matA[num1],'x',num2,'=', np.matmul(matA[num1], num2))

def main():
    result_queue = multiprocessing.Manager().Queue()
    
    matA = np.random.randint(10 ,size = (10,10))
    matB = np.random.randint(10 ,size = (10,10))
    result = np.zeros((matA.shape[0], matB.shape[1]))

    start_time = time.time()

    process = 10
    jobs = []

    for i in range(process):
        process = multiprocessing.Process(target = process_func, args= (i, result_queue, matA, matB))
        jobs.append(process)

    # for i in range(0, matA.shape[0]):
    #     thread = threading.Thread(target = thread_func, args=(i, matB, result, matA))

    
    for process in jobs:
        process.start()

    for process in jobs:
        process.join()

    while not result_queue.empty():
        result = result_queue.get()
        print(result) 

        
    print('Answer is correct:', np.all(np.matmul(matA, matB) == result))

    end_time = time.time()
    print('Time elapsed:\t', end_time - start_time)

if __name__ == "__main__":
    main()