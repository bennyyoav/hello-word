"add  new discription"

import time
import unittest

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

def sum(*args):
        sum=0
        for arg in args:
            try:
                int (arg)
            except ValueError:
                print("{} is not a valid number".format(args))
                return (-1)
            sum+=arg
        return sum
class Testfibi(unittest.TestCase):

    def test_time(self):
        start = time.time()
        fibieSerial(35)
        timeRecor = time.time() - start

        start = time.time()
        fibieSerialNotRecor(35)
        timeNotRecor = time.time() - start

        self.assertGreater(timeRecor,timeNotRecor)
    def testFibiElem(self):
        self.assertListEqual(fibieSerial(10), [0 ,1, 1,2,3,5,8,13,21,34], "fibi 1o is {} Should be 0 ,1, 1,2,3,5,8,13,21,34".format(fibieSerial(10)))

class MyParentClass():
    def __init__(self):
        print("in parent class")
    def print(self):
        print ("print")


class SubClass(MyParentClass):
    def __init__(self):
        print ("in subclass")
        super().__init__()
        super().print()



if __name__ == '__main__':
    import reader
    a=SubClass()
    print (sum(1))
    print (sum(2,1))
    print (sum(1,1,1,1,1,))
    print(sum(1, "w", 1, 1, 1, ))
    unittest.main()



