from pyspark.sql import SparkSession

def load_data(spark, file_path):
    """
    Loads data from a file using SparkSession.

    Args:
        spark (SparkSession): The SparkSession object.
        file_path (str): The path to the input file.

    Returns:
        DataFrame: The loaded data as a DataFrame.
    """
    # Load data
    data = spark.read.format("csv") \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .load(file_path)

    return data

if __name__ == "__main__":
    # Initialize SparkSession
    spark = SparkSession.builder \
        .appName("Data Loader") \
        .getOrCreate()

    # Load data from file
    file_path = "/path/to/data.csv"
    data = load_data(spark, file_path)

    # Perform further operations on the data
    # ...

    # Stop the SparkSession
    spark.stop()
