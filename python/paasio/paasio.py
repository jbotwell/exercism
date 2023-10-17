import io


class MeteredFile(io.BufferedRandom):
    """Implement using a subclassing model."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._read_bytes = 0
        self._read_ops = 0
        self._write_bytes = 0
        self._write_ops = 0

    def __enter__(self):
        return self

    def __iter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return super().__exit__(exc_type, exc_val, exc_tb)

    def __next__(self):
        line = super().readline()
        self._read_ops += 1
        self._read_bytes += len(line)
        if line:
            return line
        else:
            raise StopIteration

    def read(self, size=-1):
        total = super().read(size)

        self._read_ops += 1
        self._read_bytes += len(total)
        return total

    @property
    def read_bytes(self):
        return self._read_bytes

    @property
    def read_ops(self):
        return self._read_ops

    def write(self, b):
        size = super().write(b)

        self._write_ops += 1
        self._write_bytes += size

        return size

    @property
    def write_bytes(self):
        return self._write_bytes

    @property
    def write_ops(self):
        return self._write_ops


class MeteredSocket:
    """Implement using a delegation model."""

    def __init__(self, socket):
        self._socket = socket

        self._send_calls = 0
        self._sent_bytes = 0
        self._recv_calls = 0
        self._recv_bytes = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self._socket.__exit__(exc_type, exc_val, exc_tb)

    def recv(self, bufsize, flags=0):
        total = self._socket.recv(bufsize, flags)

        self._recv_calls += 1
        self._recv_bytes += len(total)

        return total

    @property
    def recv_bytes(self):
        return self._recv_bytes

    @property
    def recv_ops(self):
        return self._recv_calls

    def send(self, data, flags=0):
        total = self._socket.send(data, flags)

        self._send_calls += 1
        self._sent_bytes += total
        return total

    @property
    def send_bytes(self):
        return self._sent_bytes

    @property
    def send_ops(self):
        return self._send_calls
