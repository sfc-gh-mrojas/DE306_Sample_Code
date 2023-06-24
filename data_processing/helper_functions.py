from pyspark.sql.functions import col, lit, when

def calculate_total_price(quantity_col, price_col):
    """
    Calculates the total price based on the quantity and price columns.

    Args:
        quantity_col (Column): The quantity column.
        price_col (Column): The price column.

    Returns:
        Column: The column representing the total price.
    """
    total_price_col = quantity_col * price_col
    return total_price_col

def apply_discount(price_col, discount_percentage):
    """
    Applies a discount to the price based on the given discount percentage.

    Args:
        price_col (Column): The price column.
        discount_percentage (float): The discount percentage.

    Returns:
        Column: The column representing the discounted price.
    """
    discounted_price_col = when(col("category") == "Sale", price_col * (1 - discount_percentage)).otherwise(price_col)
    return discounted_price_col

if __name__ == "__main__":
    # Initialize SparkSession
    spark = SparkSession.builder \
        .appName("Helper Functions") \
        .getOrCreate()

    # Sample usage of helper functions
    data = spark.createDataFrame([
        (1, "Product A", 10, 100.0, "Regular"),
        (2, "Product B", 5, 50.0, "Sale"),
        (3, "Product C", 2, 30.0, "Regular")
    ], ["id", "product_name", "quantity", "price", "category"])

    # Calculate total price
    data_with_total_price = data.withColumn("total_price", calculate_total_price(col("quantity"), col("price")))

    # Apply discount
    discounted_data = data_with_total_price.withColumn("discounted_price", apply_discount(col("price"), lit(0.2)))

    # Display the result
    discounted_data.show()

    # Stop the SparkSession
    spark.stop()
