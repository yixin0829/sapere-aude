# Data & Analytics Basic

The markdown ultimatedly aims to summarize, consolidate basic data analysis code across all useful modules
and programming languages (e.g. Python pandas, NumPy library and R), to compare their *similarity*.

For now we focus on **R**.

## Data Structures & Data Types (R)
* Types
    * Numeric
    * Character
    * Factor: takes the categorical variable and stores data in *levels* which takes less space
    * Logical
    * Dates: just a special case of numeric
* Structures
    * Vectors
    * Matrix
    * Array
    * Data Frame
    * List

## Data Management
* Importing data into R (e.g. RODBC, CSV)
* Initial data management:
    * Look for odd/ outlier values
    * Deal with missing data
    * Merge dataframes together
* Perform analysis
* Generate results (plots, hypothesis, processed data)

### Importing Files to `Data Frame`
```r
# R
df <- read.csv('../data/df.csv') # Preferred
df_2 <- read.table('../data/df.txt', header=F, sep='|')
head(df)
tail(df)
```

### Cast Column dType & Creating new
`R`: `as.<type>(<col>)`

```r
hr_df$employee_id <- as.character(hr_df$employee_id)

# creating a new column based on others
hr_df$pSum <- hr_df$p01 + hr_df$p02 # creating "pSum" new col
names(hr_df) # print out all column names
```

### Count Unique Values (Column)
In `pandas`, we have `pandas.Series.value_counts()`.

In `R`, we have `table(df$col_name)`

### Renaming or Drop Column
```r
# by label
names(hr_df)[names(hr_df) == "age"] <- "ageRaw" 
# by indx
names(hr_df)[4] <- "ageRaw" 

# dropping column by NULL
df$col_to_drop <- NULL
```

### R `data.table`
* a `data.table` object is also a `data.frame` (can use `class()` to check equivalent of `type()` in Python)
* [Cheat sheet for R data.table](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/datatable_Cheat_Sheet_R.pdf)
* **General form:** `DT[i, j, by]`
* Creating a `data.table`
```r
# easy conversion
dt <- data.table(df)
class(dt)

# subsetting
## subset column(s)
df[, c2]
df[, .(c2, c3)]
df[, list(c2, c3)] # equiv to above

# indexing and keys
setkey(dt, c2)
dt["a"]

# doing j by group
dt[1: 1000, .(sum(c4), sd(c5)), by=c1] # calculate sum and std dev of c4 & c5 group by c1 after subsetting the first 1000 rows

```
