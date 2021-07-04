# Python Data Manipulation Basic with NumPy & pandas

## Numpy
### Creating Arrays
```python
np.random.rand(d0, d1, .. dn) # random samples from a uniform distr over [0, 1)
np.random.normal(loc=0.0, scale=1.0, size=None) # normal distr with loc(mean) and scale()
np.random.uniform(low=0.0, high=1.0, size=None) # uniform distr
```

### Reshaping and Flattening
[Reshaping and flattening multidimensional arrays](https://numpy.org/devdocs/user/absolute_beginners.html#reshaping-and-flattening-multidimensional-arrays) with `.flatten()` and `.ravel()`.

`flatten()` creates a new copy while `.ravel()` creates a "view" and is memory efficient.

## pandas
See more detailed **comparison with sql** in [here](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sql.html).

### Joining
* joining two tables with different column names with `pd.merge()`
```python
# default return a new copy of merged dataframe (copy=True)
mrg_df = df1.merge(df2, left_on='lkey', right_on='rkey', copy=True)
```
* joining two tables with `pd.df.join()`
    * `lsuffix` and `rsuffix` should be used when two tables have same column names
    * `<keys>` can be a `list` or a `str`
```python
df_caller = df_caller.join(df_other.set_index(<keys>), on=<keys>, how={'left', 'right', 'inner', 'outer'}, lsuffix='_l', rsuffix='_r')
```

### Column Manipulation
* renaming columns
    * `df.columns = ['col1', 'col2', 'col3']`
* switching columns

### Filtering
* dropping columns
    * `df = df.drop(['col1', 'col2'], axis=1)`
* dropping columns containing `NaN` with [DataFrame.dropna()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html)
* dropping rows containing `NaN` in a specific column(s) -> see `DataFrame.dropna()`
* SQL-like filtering for `Dataframe`
    * `tips[(tips["time"] == "Dinner") & (tips["tip"] > 5.00)]` where `&` acts as `AND` in SQL
    * NULL checking is done using `notna()` and `isna()` methods. `frame[frame["col1"].notna()]` is equivalent as below
```sql
SELECT *
FROM frame
WHERE col1 IS [NOT] NULL;
```

### Selection