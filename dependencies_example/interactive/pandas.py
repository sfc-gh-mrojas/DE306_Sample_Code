import pandas as pd
import symbology_mapping

# Function to load data from a CSV file into a pandas DataFrame
def load_data(file_path):
    return pd.read_csv(file_path)

# Function to save a pandas DataFrame to a CSV file
def save_data(dataframe, file_path):
    dataframe.to_csv(file_path, index=False)

# Function to check for missing values in a pandas DataFrame
def check_missing_values(dataframe):
    return dataframe.isnull().sum()

# Function to drop rows with missing values from a pandas DataFrame
def drop_missing_values(dataframe):
    return dataframe.dropna()

# Function to perform column-wise mean imputation of missing values in a pandas DataFrame
def mean_imputation(dataframe):
    return dataframe.fillna(dataframe.mean())

# Function to perform one-hot encoding on categorical columns of a pandas DataFrame
def one_hot_encoding(dataframe, columns):
    return pd.get_dummies(dataframe, columns=columns)

# Function to merge two pandas DataFrames based on a common key
def merge_data(dataframe1, dataframe2, on):
    return pd.merge(dataframe1, dataframe2, on=on)

# Function to sort a pandas DataFrame by one or more columns
def sort_data(dataframe, by):
    return dataframe.sort_values(by=by)

# Function to sample a specified number of rows from a pandas DataFrame
def sample_data(dataframe, n):
    return dataframe.sample(n=n)

# Function to calculate descriptive statistics of numerical columns in a pandas DataFrame
def describe_data(dataframe):
    return dataframe.describe()
