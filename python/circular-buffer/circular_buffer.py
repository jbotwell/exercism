class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """

    def __init__(self, message):
        self.message = message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """

    def __init__(self, message):
        self.message = message


class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []

    def read(self):
        try:
            return self.queue.pop(0)
        except IndexError:
            raise BufferEmptyException("Circular buffer is empty")

    def write(self, data):
        if len(self.queue) == self.capacity:
            raise BufferFullException("Circular buffer is full")
        else:
            self.queue.append(data)

    def overwrite(self, data):
        if len(self.queue) < self.capacity:
            self.write(data)
        else:
            self.queue.pop(0)
            self.queue.append(data)

    def clear(self):
        self.queue = []
