# Python Tips

## Knowledge Base
### Hashable Data Types
Usually *immutable* types in Python is also hashable as they will have a `__hash__()` method which
returns a hash value that NEVER changes during their lifetime. See [Python glossary](https://docs.python.org/3.8/glossary.html)

**Hashable types:** `str`, `int`, `float`, `tuple`, and `NoneType`

**Unhashable types:** `dict`, `List`, and `set`


## Technical Tricks
### Swapping
```python
# python built-in method (without temp)
x = 10
y = 20
x, y = y, x
```

### Rotating Array
```python
# Rotating right by k
n = len(arr)
k %= n
arr[:] = arr[n-k:] + arr[:n-k]
```

### Reverse Python String
The easiest and fastest way is through slicing.
```python
s = "reverse me !"
s = s[::-1] # slicing reverse ("smily reverse")
```

### Looping Backward
Note that `range()` function returns an immutable sequence type (i.e. `range` type) that excludes `stop` (similar to slicing).
Example, loop through `range(5)` will give you `0 1 2 3 4` so `stop=-1` is crucial.
```python
s = 'hello'
for i in range(len(s), -1, -1): # range(start, stop, step)
    print(s[i])
```

### Compare Two Unordered Lists
```python
a = [1, 2, 3, 1, 2, 3]
b = [3, 2, 1, 3, 2, 1]
```
`a` and `b` should be considered equal, because they have exactly the same elements, only in different order.
See [this StackOverflow post](https://stackoverflow.com/questions/7828867/how-to-efficiently-compare-two-unordered-lists-not-sets-in-python) for using `Counter()` to do it efficiently in `O(n)` time.

```python
def compare(s, t):
    # O(n) if elements are hashable
    return Counter(s) == Counter(t)
```

## pandas & NumPy Jam
Get comfortable with data manipulation, stat programming etc.
