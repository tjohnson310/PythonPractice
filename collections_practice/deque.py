# The collections.deque in Python is a specialized container datatype, pronounced "deck," and stands for "double-ended
# queue." It is part of the collections module in Pytohn's standard library.

# Key Features and Benefits:
#   - Double-Ended Operations: Unlike standard python lists, which are efficient for appending and popping elements
#   from the right end, "deque" offers efficient (O(1) complexity) appending and popping opreations from both the left
#   and right ends. This makes it ideal for implementing queues (FIFO - First In, First Out) and stacks (LIFO - Last In,
#   First Out)
#   - Memory efficiency: "deque" is implemented as a doubly-linked list, which provides memory-efficient operations
#   compared to lists when frequent insertions or deletions occur at the beginning of the sequence.
#   - Thread safety: "deque operations are atomic, meaning they are designed to be safe for use in multithreaded
#   environments without requiring explicit locking mechanisms for basic operations.
#   - maxlen Parameter: deques can be initialized with a maxlen parameter, which limits their size. When the deque
#   reaches this maximum length, adding new elements automatically removes elements from the opposite end, maintaining
#   the fixed size.

# Common Use Cases:
# Queues: Implement FIFO data structures where elements are added to one end and removed from the other.
# Stacks: Implement LIFO data structures where elements are added and removed from the same end.
# Sliding Window problems: Efficiently manage a window of elements in algrithms that require processing a fixed-size
# subset of data.
# Real-time data processing: handle streams of data where elements need to be added and removed wuickly from either end.

# Basic usage example:
from collections import deque

# Create a deque
my_deque = deque([1, 2, 3])

# Add elements
my_deque.append(4)
my_deque.appendleft(0)
print(f"Deque after appending: {my_deque}")

# Remove elements
popped_right = my_deque.pop()
popped_left = my_deque.popleft()
print(f"Deque after popping: {my_deque}")
print(f"Popped from right: {popped_right}, Popped from left: {popped_left}")

# Rotate the deque
my_deque.rotate(1)
print(f"Deque after rotating: {my_deque}")
