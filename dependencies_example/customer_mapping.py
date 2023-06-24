from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when
import interactive.pandas
import utils.pyspark_test
import utils_algo
import product_mapping


# Create a SparkSession
spark = SparkSession.builder.getOrCreate()

# Create sample customer data
customer_data = [("John", 25, "USA"), ("Alice", 30, "Canada"), ("Bob", 35, "USA"), ("Charlie", 40, "UK")]
customer_df = spark.createDataFrame(customer_data, ["name", "age", "country"])

# Define customer mapping
mapping = {
    "USA": "North America",
    "Canada": "North America",
    "UK": "Europe"
}

# Apply customer mapping
customer_mapped_df = customer_df.withColumn("continent", when(col("country").isin(mapping.keys()), mapping[col("country")]).otherwise("Unknown"))

# Display the mapped customer data
customer_mapped_df.show()
