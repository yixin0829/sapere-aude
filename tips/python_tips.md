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
The easiest way is through slicing. It creates a new copy for the storing the variables inside iterable. The format[a : b : c] in slicing states that from an inclusive to b exclusive, count in increments of c. In above code, a and b is blank and c is -1. So it iterates the entire list counting from the last element to the first element resulting in a reversed list.
```python
s = "reverse me !"
ls = [1, 2, 3, 4, 5] 
s = s[::-1] # slicing reverse ("smily reverse")
ls = ls[::-1] # return a new copy
```

The **fastest** way to reverse is to user built-in function `reversed()` since it returns a `reverseiterator` object to allow you loop backwards without copying any variables.
```python
ls = [1, 2, 3, 4, 5]
print(ls) # <list_reverseiterator object at 0x7fbd84e0b630>
ls_iter = reversed(ls)
for ele in ls_iter:
    print(ele)
```


### Looping Backward
Note that `range()` function returns an immutable sequence type (i.e. `range` type) that excludes `stop` (similar to slicing).
Example, loop through `range(5)` will give you `0 1 2 3 4` so `stop=-1` is crucial.
```python
# method 1: use range() function
s = 'hello'
for i in range(len(s), -1, -1): # range(start, stop, step) -1 is crucial
    print(s[i])

# method 2: use reversed() function (preferred)
for c in reversed(s):
    print(c)
```

### Looping with 2 Ptrs
One increasing and the other decreasing. Can use built-in `zip()` function to [zip](https://docs.python.org/3/library/functions.html#zip) iterables together.
```python
# i count up and j count down
left, right = 1, 5
for i, j in zip(range(left, right), range(right, left, -1)):
    print(f'i: {i} | j: {j} ')
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

### Initialize `inf`
useful when try to init sth large to track the smallest value as python int has arbitrary precision (note: numpy & pandas are different since
they use C-style fixed-precision integers)
```python
diff = float('inf')
if new < diff:
    diff = new
```

### `bisect` Module (for binary search)
`bisect()`, `bisect_left()`, `bisect_right()` are useful to speed up binary search problem (one line code). `insort()` returns the list
after it's inserted. see more details in [here](https://www.geeksforgeeks.org/bisect-algorithm-functions-in-python/)

[code snippet to run](../snpts/bsct.py)
```python
def bs(nums: List[int], tar: int) -> int:
    # return the left most index to insert
    return bisect_lef(nums, tar)
```

### Unique List/String & Filtering Dups
Using `len()` and `set()`. Can also use the same trick to filter out duplicates in a list.
```python
# pythonic way (fastest)
a = "hello"
b = [1, 2, 3, 4, 5]
len(set(a)) == len(a) # return False
len(set(b)) == len(b) # return True

# filtering duplicates
l = [1, 1, 2]
l = list(set(l)) # return [1, 2]
```

### Initializing 1D & 2D Array (Preferred Ways)
See more details in this GeeksforGeeks [article](https://www.geeksforgeeks.org/python-which-is-faster-to-initialize-lists/).
In general we prefer to use `*` operator when init 1D array and list comprehension when init 2D array since `*` will create a shallow list see this
GeeksforGeeks [article](https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/) about 2D array in python
```python
# for 1D array [object] * num
arr = [0] * 1000

# for 2D array
## Using * operator would create shallow lists
arr = [[0]*no_of_cols]*no_of_rows

## Using list comprehensions is better for 2d arrays
arr = [[0 for i in range(no_of_cols)] for j in range(no_of_rows)]
```

## Techniques
### Two-pointer
Check out a beginner refresher in [this article](https://medium.com/swlh/two-pointer-technique-solving-array-problems-at-light-speed-56a77ee83d16)

### Runner (Linked List)


## pandas & NumPy Jam
Get comfortable with data manipulation, stat programming etc.
