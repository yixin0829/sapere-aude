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

### Exploring the data
* `df.describe()`: sumamry statistics of columns
* `df[col_list]`: select column(s) of interest
* `df.info()`/`df.dtypes`: summary of the Dataframe (data types)
* `df.shape`: tuple in format of (rows, cols)
* `Series.value_counts(normalize=False, sort=True, ascending=False, bins=None, dropna=True)`
    * Return a Series containing counts of unique values.
    * `nomalized=True` will return relative frequency (percentage)

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

* joining data frames with  `df1.merge(df2, join_field, join_type)`
    * join_field: `on='field'` (fields are equal), `left_on='field_1'`, `right_on='field_2'` (join on different fields)
    * join_type: `how='inner'/'left'/'right'/'outer'`

### Column Manipulation
* renaming columns
    * `df.columns = ['col1', 'col2', 'col3']`
```python
df.rename(columns={
    'current_col': 'new_col_name'
})
```
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

## Plotting
* x label rotation: `plt.xticks(rotation=45)`
* Always use `plt.show()` at the end to show plots

### Correlation Heatmap
* using `.set_xticklabels()` to rotate x-labels to avoid mis-alignment
```py
metrics = df.iloc[:, 6:-1]
corr = metrics.corr().round(2)
fig, ax = plt.subplots(figsize=(20, 12))
g = sns.heatmap(ax=ax, data=corr, annot=True)
g.set_xticklabels(g.get_xticklabels(), rotation=45, horizontalalignment='right')
plt.show()
fig.savefig("corr.png")
```