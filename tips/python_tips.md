# Python Tips

## Swapping
```python
# python built-in method (without temp)
x = 10
y = 20
x, y = y, x
```

## Rotating Array
```python
# Rotating right by k
n = len(arr)
k %= n
arr[:] = arr[n-k:] + arr[:n-k]
```
