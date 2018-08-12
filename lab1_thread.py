import numpy as np
import threading
import time

s = 10

def thread_func(matA_row, matB, result, matA):
    result[matA_row] = np.matmul(matA[matA_row], matB)
    #     result[row] = np.matmul(matA[row], matB)
    # print(matA[num1],'x',num2,'=', np.matmul(matA[num1], num2))

def main():

    matA = np.random.randint(10 ,size = (s,s))
    matB = np.random.randint(10 ,size = (s,s))
    result = np.zeros((matA.shape[0], matB.shape[1]))

    start_time = time.time()

    thread = 10
    threads = []
    
    for i in range(0, matA.shape[0]):
        thread = threading.Thread(target = thread_func, args=(i, matB, result, matA))
        threads.append(thread)

    for thread in threads:
        thread.start()
    
    for thread in threads:
        thread.join()
    
    print('Answer is correct:', np.all(np.matmul(matA, matB) == result))

    end_time = time.time()
    print('Time elapsed:\t', end_time - start_time)

if __name__ == "__main__":
    main()



