from multiprocessing import Process, Manager

from random import random
import time

def func1(array):    

    
    while True:
        for i in range(len(array)):
            print("func1 number ",i,": ",array[i])

        print("\n")

        time.sleep(1)


def func2(array):   

    while True: 

        for i in range(len(array)):

            randnum = random()*100
            #print("func2 number ",i,": ", randnum)
            array[i] = randnum

        time.sleep(1) 



if __name__ == '__main__':
    
    with Manager() as manager:

       array = manager.list([500,500,500]) 

       process1 = Process(target = func1, args = (array,))

       process2 = Process(target = func2, args = (array,))

       process2.start()
   


       process1.start()
       process1.join()
       process2.join()

       #print(array)
       


   

  

#from multiprocessing import Process, Manager

# def f(d, l):
#     d[1] = '1'
#     d['2'] = 2
#     d[0.25] = None

#     print(l)
#     l.reverse()

# if __name__ == '__main__':
#     with Manager() as manager:
#         d = manager.dict()
#         l = manager.list(range(10))

#         p = Process(target=f, args=(d, l))
#         p.start()
#         p.join()

#         print(d)
#         print(l)
       

