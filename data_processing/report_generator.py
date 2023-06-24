import pandas as pd

def generate_report(data):
    """
    Generates a report based on the input data.

    Args:
        data (DataFrame): The input data as a DataFrame.
    """
    # Convert Spark DataFrame to Pandas DataFrame
    pandas_df = data.toPandas()

    # Perform data analysis and generate report
    report = pandas_df.describe()

    # Save the report to a file
    report.to_csv("report.csv", index=False)

if __name__ == "__main__":
    # Initialize SparkSession
    spark = SparkSession.builder \
        .appName("Report Generator") \
        .getOrCreate()

    # Sample usage of generate_report function
    data = spark.createDataFrame([
        (1, "Product A", 10),
        (2, "Product B", 5),
        (3, "Product C", 2),
        (4, "Product D", 8),
        (5, "Product E", 12)
    ], ["id", "product_name", "quantity"])

    # Generate the report
    generate_report(data)

    # Stop the SparkSession
    spark.stop()
