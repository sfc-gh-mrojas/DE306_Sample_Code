from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when
import decorators

# Create a SparkSession
spark = SparkSession.builder.getOrCreate()

# Create sample symbol data
symbol_data = [("AAPL", "Apple Inc."), ("GOOG", "Alphabet Inc."), ("MSFT", "Microsoft Corporation"), ("AMZN", "Amazon.com, Inc.")]
symbol_df = spark.createDataFrame(symbol_data, ["symbol", "company"])

# Define symbol mapping
mapping = {
    "AAPL": "Apple",
    "GOOG": "Google",
    "MSFT": "Microsoft",
    "AMZN": "Amazon"
}

# Apply symbol mapping
symbol_mapped_df = symbol_df.withColumn("mapped_company", when(col("symbol").isin(mapping.keys()), mapping[col("symbol")]).otherwise("Unknown"))

# Display the mapped symbol data
symbol_mapped_df.show()
