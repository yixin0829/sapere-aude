# Data and Analytics (Data Science Technical Interview)

This directory dedicates to ds-related technical learning, for example, data manipulation with `pandas`, matrix calculation and hypothesis testing with `numpy` and `scipy`, visualization with `matplotlib`, basic modeling with `sklearn` (in Python), and different machine/deep learning algorithms learned along the journey.

To be consistent we will choose Python as the main programming language.

## Statistics
* [Statistical Thinking in 21st Century Python example (dm, plot, testing)](https://colab.research.google.com/drive/1ykIr4FUikZNY41yihStRraxsUCve71pt?usp=sharing)
* A list of key concepts in statistics for DS. In general we have frequentist interpretation and Bayesian interpretation
* [Fitting models to data](https://statsthinking21.github.io/statsthinking21-core-site/fitting-models.html#what-is-a-model)
    * Mean, median (less sensitive to outliers), and mode
    * Variability (variance aka $\sigma^2 = \frac{\sum_{i=1}^n(x_i - \mu)^2}{N}$)
        * When computing estimated var based on a sampled population, sample will "lost" a degree of freedom since we used a data point to estimate the mean
    * Standard deviation ($\sigma$)
    * Z-score $Z(x) = \frac{x - \mu}{\sigma}$: Intuitively, you can think of a Z-score as telling you how far away any data point is from the mean using stdev as unit (e.g. Z-score = 2 that means the data is 2 stdev)
        * Using Z-scores to compare distribution
    * F1-score $F_1 = 2 \cdot \frac{precision \cdot recall}{precision + recall} = 2 \cdot \frac{TP}{ TP + \frac{1}{2}(FP + FN)}$
        * Used to measure binary classification model. It's the **harmonic mean** of the precision and recall. A perfect model has an F-score of 1.
        * precision: the number of true positives divided by the number of false positives plus true positives.
        * recall: actual coverage of all the positive samples
* [Hypothesis testing](https://statsthinking21.github.io/statsthinking21-python/08-HypothesisTesting.html)
    * **null hypothesis (no difference)** and **alternative hypothesis**
    * **t test**
    * **p-value**: quantify how confident we should that two populations are different
    * **type I error (alpha aka significance level):** the probability of false rejection of the null hypothesis (**false positive**)
    * **type II error (beta):** the probability of false acceptance of the null hypothesis (**false negative**)
* Statistical power analysis
    * power = 1 - beta

### Stat Power & Hypothesis Testing
* see this article about [different tests](https://www.scribbr.com/statistics/statistical-tests/)
    * regression tests
        * linear regression
        * logistic regression
    * comparison tests
        * t-test
        * ANOVA
    * correlation tests
        * pearson's r'
    * non-parametric tests
        * Chi Square
        * Welcoxon Rank-Sum test
* see [intro to stats power and power analysis](https://machinelearningmastery.com/statistical-power-and-power-analysis-in-python/) using Python
* type I error: false positive
    * the type I error rate is ($\alpha$)
    * **significance level** ($\alpha$): risk of obtaining a false positive, usually predetermined (e.g. 0.05)
    * **p-value** (p): Probability of obtaining a result equal to or more extreme than was observed in the data
* type II error: false negative
    * the type II error rate is ($\beta$)
    * **statistical power**: The risk of a Type II error is inversely related to the statistical power of a study. The higher the statistical power, the lower the probability of making a Type II error.
        * $Power = 1 - \beta$
* trade-off b/w type I and type II errrors
    * usually we try to avoid type I more (more conservative about rejecting null hypothesis). A Type I error means mistakenly going against the main statistical assumption of a null hypothesis. This may lead to new policies, practices or treatments that are inadequate or a waste of resources.

### Beta, Alpha, R-Squared
* **beta** - indicates how closely its price follows the same pattern as a relevant index over time (see more details [here](https://www.investopedia.com/terms/b/beta.asp))
    * equal to 1.0 - strongly correlated with the market
    * less than 1.0 - the security is theoretically less volatile than the market
    * greater than 1.0 - more volatile than the market (e.g. beta=1.2 meaning assumed to be 20% more volatile than the market)
    * negative beta - inversed correlation
* **R-squared** - indicates how closely alpha and beta reflect a stock's return as opposed to how much is random or due to other unobserved factors

### Multicollinearity
* [Multicollinearity](https://statisticsbyjim.com/regression/multicollinearity-in-regression-analysis/) occurs when independent variables in a regression model are correlated
* Cause problem mainly when interpret the results of regression analysis
    * the coefficient estimates can swing wildly
    * weakens the statistical power of the regression model
* To detect: use [Variance Inflation Factor (VIF)](https://etav.github.io/python/vif_factor_python.html)

## Probability
* Conditional probability: $P(A|B) = \frac{P(A \cap B)}{P(B)}$
* Independence: $P(A|B) = P(A)$
* Inversing a condition probability: **Bayes' Rule**

## Data Manipulation
### Handle Missing Data (Imputation)
* [6 Different Ways to Compensate for Missing Values In a Dataset](https://towardsdatascience.com/6-different-ways-to-compensate-for-missing-values-data-imputation-with-examples-6022d9ca0779)
* imputation using mean/Median values
* imputation using most frequent or (zero/constant) values
* imputation using K-NN
* imputation using deep learning


## Machine Learning Algo
Notes, code snippets, math when learning new machine learning algorithms.

### Decision Tree
* [code tutorial link](https://machinelearningmastery.com/implement-decision-tree-algorithm-scratch-python/)
* [math behind the algo](https://ankitnitjsr13.medium.com/math-behind-decision-tree-algorithm-2aa398561d6d)
* usage: classification and regression
* pros
    * easy to interpret the final model
    * provide more advanced ensemble methods such as bagging, random forests and gradient boosting

