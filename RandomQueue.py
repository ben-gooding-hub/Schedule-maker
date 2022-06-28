import random


class RandomQueue:
    __queue: list
    __originalQueue: list

    def __init__(self, queue):
        self.__originalQueue = queue
        self._set_queue()

    def next(self):
        try:
            return self.__queue.pop()
        except IndexError:
            self._set_queue()
            return self.__queue.pop()

    def _set_queue(self):
        random.shuffle(self.__originalQueue)
        self.__queue = self.__originalQueue



