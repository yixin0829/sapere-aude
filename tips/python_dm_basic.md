# Python Data Manipulation Basic with NumPy & pandas

## Numpy
### Creating Arrays
```python
np.random.rand(d0, d1, .. dn) # random samples from a uniform distr over [0, 1)
np.random.normal(loc=0.0, scale=1.0, size=None) # normal distr with loc(mean) and scale()
np.random.uniform(low=0.0, high=1.0, size=None) # uniform distr
```

## pandas
### Joining
* joining two tables with different column names with `pd.merge()`
```python
# default return a new copy of merged dataframe (copy=True)
mrg_df = df1.merge(df2, left_on='lkey', right_on='rkey', copy=True)
```
* other methods