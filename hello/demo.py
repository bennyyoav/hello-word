"add  new discription"

import time


def twice(x):
    return 2 * x


def printHello():
    return ("hello")


def fibielemReq(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibielemReq(num - 1) + fibielemReq(num - 2)


def fibieSerialNotRecor(size):
    fibiSerial = []
    for elem in range(size):
         fibiSerial.append(notRecorFib(elem))
    return fibiSerial

def fibieSerial(size):
    fibiSerial = []
    for elem in range(size):
      fibiSerial.append(fibielemReq(elem))
    return fibiSerial


def notRecorFib(n):
    prevElem, elem = 0, 1
    for i in range(n):
        prevElem, elem = elem, prevElem + elem
    return prevElem





if __name__ == "__main__":
    start = time.time()
    fibieSerial(35)
    timeRecor = time.time() - start



  
    start = time.time()
    fibieSerialNotRecor(35)
    timeNotRecor = time.time() - start

    print("tinerecor {}, time not recor{} deff is = {}".format(timeRecor,timeNotRecor,timeRecor - timeNotRecor))

    # assert ((fibieSerial(10)) == [0 ,1, 1,2,3,5,8,13,21,34]),"{}".format((fibieSerial(10)))
    # assert (fibieSerial(10)==fibieSerialNotRecor(10))

