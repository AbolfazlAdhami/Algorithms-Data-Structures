from collections import deque
from typing import Deque, Any


class Queue:
    def __init__(self) -> None:
        self._data: Deque[Any] = deque()

    def enqueue(self, item: Any) -> None:
        self._data.append(item)

    def dequeue(self) -> Any:
        return self._data.popleft()

    def peek(self) -> Any:
        return self._data[0]

    def size(self) -> int:
        return len(self._data)

    def is_empty(self) -> bool:
        return not self._data

    def __repr__(self) -> str:
        # shows contents as Queue([a, b, c])
        return f"Queue({list(self._data)})"


def solve(cmd: list[str], queue: Queue) -> None:
    op = cmd[0]
    if op == 'enqueue':
        if len(cmd) < 2:
            print("Error: missing value to enqueue")
            return
        queue.enqueue(cmd[1])
        print(queue)
    elif op == 'dequeue':
        if queue.is_empty():
            print("Oops!")
        else:
            print(queue.dequeue())
    elif op == 'peek':
        print('None' if queue.is_empty() else queue.peek())
    elif op == 'size':
        print(queue.size())
    elif op == 'empty':
        print(queue.is_empty())
    else:
        print("Unknown command:", op)


def main() -> None:
    q = Queue()
    while True:
        try:
            cmd = input().split()
        except EOFError:
            break

        if not cmd:
            continue
        if cmd[0] == 'quit':
            break

        solve(cmd, q)


if __name__ == "__main__":
    main()
