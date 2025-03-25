"""Queue implementation with 2 stacks."""


class Queue:
    """Queue implemented with 2 stacks."""

    def __init__(self, elems: list[int] | None = None) -> None:
        self.end: list[int] = elems or []
        self.beginning: list[int] = []

    def push(self, x: int) -> None:
        """Push x to the end of the queue."""
        self.end.append(x)

    def pop(self) -> int:
        """Pop the first item of the queue."""
        if not self.beginning:
            while self.end:
                self.beginning.append(self.end.pop())
        return self.beginning.pop()

    def __len__(self) -> int:
        return len(self.end) + len(self.beginning)
