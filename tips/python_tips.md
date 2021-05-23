# Python Tips

## Technical

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

## pandas & NumPy Jam
Get comfortable with data manipulation, stat programming etc.
