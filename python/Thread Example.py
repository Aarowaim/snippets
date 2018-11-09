from threading import Thread
import time


def main_loop():
    mythread = LedThread()
    mythread.start()

    time.sleep(20)
    mythread.stop()


class LedThread(Thread):

    def __init__(self):
        super(LedThread, self).__init__()
        self._keepgoing = True

    def run(self):
        while (self._keepgoing):
            time.sleep(0.5)
            print('Blink')

    def stop(self):
        self._keepgoing = False


main_loop()
