Pandas Training:
pip or conda can be used to install packages like pandas, matplotlib etc
Python version used: 3.10.2
1. Installing Anaconda
### From Website
https://www.anaconda.com/download

2. Install or use Jupyter Notebook
### From Anaconda: 
jupyter notebook comes by default with ananconda
### using pip
pip install notebook

3. Run Jupyter notebook
From Command line: jupyter notebook
From Anoconda: Select jupyter notebook and launch

Use shift + Enter to run a cell


### Pandas
#### Importing Pandas
1. Import pandas and to call anyuse pandas.<method_name>
2. Import pandas as pd and to call any method pd.<method_name>

#### Pandas Documentation
- pd.<TABKEY>
- pd?

### Series and DataFrame
Dataframe: is like a two dimmensional array, it is a sequence of series which share same index
e.g. df=pd.readcsv("pathtoFile")
Series: A one dimensional array of indexed data
e.g. df['column_name']  or df["column_name"] or df.column_name
df[["colum1","column2'"]]

Using type():
type(DataFrame)
type(DataFrame.SeriesName)
type(DataFrame[["Column1","Column2"]]


### Data Input and Validation:
#### Input
- read_excel(..)
- read_json(..)
- read_sql_table(..)

- Read csv to dataframe
	df=pd.read_csv('../data/input.csv')

#### Shape : To get Dimensions
Dataframe.shape
Dataframe.shape[columnIndex]


#### Head: top rows or top n rows(default 5)
df.head() or df.head(10)

#### Tail: bottom rows or bottom n rows(default 5)
df.tail() or df.tail(10)

#### Info: Information about dataframe including all columns, non null count, Dtype
df.info()

### Data Analysis

#### value_counts(): normalize=False, sort=True, ascending=False, bins=None, dropna=True
- return a object containing count of unique values, default is descending
e.g. df.Gender.value_counts(ascending=True, dropna=False)

#### sort_values(): axis=0, ascending=true
df.city.sort_values()

#### boolean indexing: vectors to filter data
operator: and(&), or(|) and Not (~)

#### String Handling:
Builtin string method of str attribute
e.g startsWith(), endsWith()
df[df.Athlete.str.contains('Florence')]


### Basic Plotting

#### Matplotlib
import matplotlib.pyplot as plt
%matplotlib inline

- plot types: kind='line' or 'bar' or 'barh' or 'pie'
e.g. plot(kind='line')
- Colors
- figsize
- colormaps
- seaborn basic plotting

### Indexing
Index object is an immutable array
Indexing allows you to access a row or column using label


### GROUP BY



### Reshaping


### Data Visualization


General issues:
1. ModuleNotFoundError: No module named 'pandas'
Suggests pandas is not installed, so either install pandas manually using
pip3 install pandas == 1.3.4
or
pip3 install pandas

2. ModuleNotFoundError: No module named 'matplotlib'
Suggests to install matplotlib, can be installed using 
pip3 install matplotlob ==version
or
pip3 install matplotlob

3. ModuleNotFoundError: No module named 'seaborn'
Suggest to install seaborn, can be installed using pip3
pip3 install seaborn == versionnumber
or
pip3 install seaborn
