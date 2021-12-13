# Data and Analytics (Data Science Technical Interview)

This directory dedicates to ds-related technical interview problems, for example, data manipulation with `pandas`, matrix calculation and hypothesis testing with `numpy` and `scipy`, visualization with `matplotlib`, and basic modeling with `sklearn` (in Python).

To be consistent we will choose Python as the main programming language for all technical interview questions.

## Google Colab Portal
* [Statistical Thinking in 21st Century Python example (dm, plot, testing)](https://colab.research.google.com/drive/1ykIr4FUikZNY41yihStRraxsUCve71pt?usp=sharing)

## Statistics
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

## Probability
A list of key concepts in probability for DS:
* Conditional probability: $P(A|B) = \frac{P(A \cap B)}{P(B)}$
* Independence: $P(A|B) = P(A)$
* Inversing a condition probability: **Bayes' Rule**
