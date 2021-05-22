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

## pandas & NumPy Jam
Get comfortable with data manipulation, stat programming etc.
