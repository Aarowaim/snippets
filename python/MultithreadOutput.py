import queue, threading
import time, sys
import random

q = queue.Queue()
keepRunning = True


def loop_output():
    thread_outputs = dict()

    while keepRunning:
        try:
            thread_id, data = q.get_nowait()
            thread_outputs[thread_id] = data
        except queue.Empty:
            # because the queue is used to update, there's no need to wait or block.
            pass

        pretty_output = ""
        for thread_id, data in sorted(thread_outputs.items()):
            pretty_output += '({}:{}) '.format(thread_id, str(data))

        sys.stdout.write('\r' + pretty_output)
        sys.stdout.flush()
        time.sleep(1)


def loop_count(thread_id, increment):
    count = 0
    while keepRunning:
        msg = (thread_id, count)
        try:
            q.put_nowait(msg)
        except queue.Full:
            pass

        count = count + increment
        time.sleep(0.01 * random.randint(1, 100))


if __name__ == '__main__':
    try:
        th_out = threading.Thread(target=loop_output)
        th_out.start()

        # make sure to use args, not pass arguments directly
        threads = []
        for i, increment in enumerate([1, 2, 5, 7]):
            th = threading.Thread(target=loop_count, args=("Thread" + str(i), increment))
            th.daemon = True
            threads.append(th)
            th.start()

        while True:
            time.sleep(.1)

    except KeyboardInterrupt:
        print("Ended by keyboard stroke")
        keepRunning = False
        for th in threads:
            th.join()
