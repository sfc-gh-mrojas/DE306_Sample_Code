from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when
import constants

# Create a SparkSession
spark = SparkSession.builder.getOrCreate()

# Create sample product data
product_data = [("Apple", "Fruit"), ("Carrot", "Vegetable"), ("Chicken", "Meat"), ("Milk", "Dairy")]
product_df = spark.createDataFrame(product_data, ["name", "category"])

# Define product mapping
mapping = {
    "Fruit": "Produce",
    "Vegetable": "Produce",
    "Meat": "Protein",
    "Dairy": "Dairy"
}

# Apply product mapping
product_mapped_df = product_df.withColumn("department", when(col("category").isin(mapping.keys()), mapping[col("category")]).otherwise("Other"))

# Display the mapped product data
product_mapped_df.show()
