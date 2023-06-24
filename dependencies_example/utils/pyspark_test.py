from pyspark.sql import SparkSession
import pytest

# Create a SparkSession
spark = SparkSession.builder.getOrCreate()

# Define a test function
def test_data_count():
    data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
    df = spark.createDataFrame(data, ["name", "age"])
    
    # Assert the count of rows in the DataFrame
    assert df.count() == 3

def test_data_filter():
    data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
    df = spark.createDataFrame(data, ["name", "age"])
    
    # Filter the DataFrame and assert the count of rows
    filtered_df = df.filter(df.age > 30)
    assert filtered_df.count() == 1
