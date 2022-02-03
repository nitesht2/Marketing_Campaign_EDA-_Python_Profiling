## Marketing_Campaign_EDA_Pandas_Profiling

Pandas_Profiling generates profile reports from a pandas DataFrame. The pandas df.describe() function is great but a little basic for serious exploratory data analysis. pandas_profiling extends the pandas DataFrame with df.profile_report() for quick data analysis.

### **In this project I have used Marketing dataset for analysis.**

For each column the following statistics and at the end it can be presented in an interactive HTML report:

#### Type inference: 
detect the types of columns in a dataframe.

#### Essentials: 
type, unique values, missing values

#### Quantile statistics:
minimum value, Q1, median, Q3, maximum, range, interquartile range

#### Descriptive statistics:
mean, mode, standard deviation, sum, median absolute deviation, coefficient of variation, kurtosis, skewness

#### Most frequent values:

#### Histograms:

#### Correlations:
highlighting of highly correlated variables, Spearman, Pearson and Kendall matrices

#### Missing values:
matrix, count, heatmap and dendrogram of missing values

#### Duplicate rows:
Lists the most occurring duplicate rows

## Installation
### Using pip: 
pip install -U pandas-profiling[notebook]

jupyter nbextension enable --py widgetsnbextension
