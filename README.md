# python-stack

A simple, from-scratch implementation of the **Stack** data structure in Python, built on a **fixed-size** list. The size is chosen when the stack is created and never changes — when the stack is full, new items are rejected.

## What is a Stack?

A stack is a linear data structure that follows the **LIFO** principle (*Last In, First Out*): the last item you add is the first one you remove. Think of a stack of plates — you can only add or remove from the top.

## Features

- `push` — add an item to the top of the stack (prints a message if the stack is full)
- `pop` — remove and return the top item (prints a message if the stack is empty)
- `peak` — view the top item without removing it
- `is_empty` — check if the stack has no items
- `show_size_top` — see how many slots are filled vs. empty
- `__len__` — use Python's built-in `len()` to get the number of items

## Installation

No dependencies needed — just Python 3. Clone the repo or copy `stack.py` into your project.

```bash
git clone https://github.com/soshjant/python-stack.git
```

## Usage

The size is optional and defaults to `10`. Once chosen, it never changes.

```python
from stack import stack

s = stack(3)   # a stack that can hold at most 3 items
# s = stack() would create a stack with the default size of 10

s.push(10)
s.push(20)
s.push(30)
s.push(40)     # prints: stack is full (the item is not added)

print(s.peak())            # 30
print(s.show_size_top())   # (3, 0)  -> 3 filled, 0 empty
print(len(s))              # 3

print(s.pop())             # 30
print(s.show_size_top())   # (2, 1)  -> 2 filled, 1 empty
print(s.is_empty())        # False
```

## How it works

The stack uses a plain Python list pre-filled with `None` and an index called `top` that points to the last filled slot:

```
size = 5, after pushing 10, 20, 30

index:   0    1    2     3     4
list:  [10,  20,  30, None, None]
                  ↑
               top = 2
```

- `push` moves `top` up by one and writes the new item there.
- `pop` returns the item at `top`, then moves `top` down by one.
- When `top == -1` the stack is empty; when `top == size - 1` it is full.

## Class Reference

| Method | Description |
|---|---|
| `stack(size=10)` | Creates a new stack that can hold `size` items (default: 10) |
| `push(x)` | Adds `x` to the top; prints `stack is full` if there is no space |
| `pop()` | Removes and returns the top item; prints `stack is empty` if empty |
| `peak()` | Returns the top item without removing it; prints `stack is empty` if empty |
| `is_empty()` | Returns `True` if the stack has no items |
| `show_size_top()` | Returns a tuple: `(filled_slots, empty_slots)` |
| `len(stack)` | Returns the number of items currently in the stack |

## Notes

- This project was built as a learning exercise to understand how a stack works internally.
- Popped items are not physically cleared from the internal list; only the `top` pointer moves. This is normal and doesn't cause any bugs.
- A version of this stack that grows automatically when full (dynamic resizing) is also possible — see the `python-dynamic-stack` project.

## License

Feel free to use, modify, and learn from this code.
