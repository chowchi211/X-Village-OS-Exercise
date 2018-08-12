import numpy as np
import time

def main():

    start_time = time.time()

    matA = np.random.randint(10 ,size = (10,10))
    matB = np.random.randint(10 ,size = (10,10))
    result = np.zeros((matA.shape[0], matB.shape[1]))

    for row in range(0, matA.shape[0]):
        result[row] = np.matmul(matA[row], matB)
    
    print('Answer is correct:', np.all(np.matmul(matA, matB) == result))
    # print(result)
    end_time = time.time()
    print('Time elapsed:\t', end_time - start_time)
if __name__ == "__main__":
    main()
