"""
Binary heap implementation.

Heap property (min heap):
- All children of a node are greater than or equal to the node

- Heapify: O(n): repeatedly heapify down starting from index n // 2 to index 0
- Heappush: O(log(n)) - push at the end and bubble up
- Heappop: O(log(n)) - swap the last and first and bubble down


Use cases:
- Priority queue (min heap)
- Quick access to min/max

Operations:
- Heapify: O(n) if implemented with heapify down
- Pop: O(log(n))
- Push: O(log(n))


Tips:
- parent(i) = (i - 1) // 2 -> max(0, (i - 1))
- children(i) = (i * 2 + 1, i * 2 + 2) + BOUNDS
- push and heapify up on len - 1
- pop and heapify down only if non empty
    - when heapifying down, don't, remember to check for bounds -> bounds in _children function
- Heapify: heapify down i for i in reversed(range(n // 2))

[1 2 3 4 5]
1
2   3
4 5 6 7


"""


class MinHeap:
    """Min heap."""

    def __init__(self, arr: list[int] | None = None) -> None:
        self.arr: list[int] = arr or []
        self._heapify()

    def push(self, val: int) -> None:
        """Push val into the heap."""
        self.arr.append(val)
        self._heapify_up(len(self.arr) - 1)
        print(self.arr)

    def pop(self) -> int:
        """Pop and return the minimum value of the heap."""
        val = self.arr[0]
        self.arr[0] = self.arr[-1]
        self.arr.pop()
        if self.arr:
            self._heapify_down(0)

        print(self.arr)
        return val

    def _heapify_up(self, i: int) -> None:
        par_i = max(0, (i - 1))
        while self.arr[par_i] > self.arr[i]:
            self.arr[par_i], self.arr[i] = self.arr[i], self.arr[par_i]
            i = par_i
            par_i = max(0, (i - 1))

    def _heapify_down(self, i: int) -> None:
        lchild, rchild = self._children(i)
        min_child = lchild if self.arr[lchild] < self.arr[rchild] else rchild
        while self.arr[min_child] < self.arr[i]:
            self.arr[min_child], self.arr[i] = self.arr[i], self.arr[min_child]
            i = min_child
            lchild, rchild = self._children(i)
            min_child = lchild if self.arr[lchild] < self.arr[rchild] else rchild

    def _heapify(self) -> None:
        print(self.arr)
        for i in reversed(range(len(self.arr) // 2)):
            self._heapify_down(i)
            print(self.arr)

    def _children(self, i: int) -> tuple[int, int]:
        lchild, rchild = (i * 2 + 1, i * 2 + 2)
        n = len(self.arr)
        return lchild if lchild < n else i, rchild if rchild < n else i


h = MinHeap()
h.push(3)
h.push(1)
h.push(2)
print(h.pop())

h = MinHeap([3, 2, 6, 7, 9, 1])
