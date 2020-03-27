import time
import threading
def makeTimer():
    lastCalled=None
    def elapsed():
        nonlocal lastCalled
        now = time.time()
        if lastCalled is None:
            lastCalled=now
            return None
        result = now - lastCalled
        lastCalled = now
        return result
    return  elapsed

if __name__==__main__:
    t=makeTimer()
    print (t())
    time.sleep(1)
    print (t())
    time.sleep(1)
    print (t())
    time.sleep(1)
    print (t())
