import matplotlib.pyplot as plt

def plot_histogram(data, column):
    """
    Plots a histogram for the specified column of the input data.

    Args:
        data (DataFrame): The input data as a DataFrame.
        column (str): The column name for which to plot the histogram.
    """
    # Extract column values for plotting
    column_data = data.select(column).rdd.flatMap(lambda x: x).collect()

    # Create a histogram plot
    plt.hist(column_data, bins=10, edgecolor='black')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.title(f'Histogram of {column}')
    plt.show()

if __name__ == "__main__":
    # Initialize SparkSession
    spark = SparkSession.builder \
        .appName("Data Visualization") \
        .getOrCreate()

    # Sample usage of plot_histogram function
    data = spark.createDataFrame([
        (1, "Product A", 10),
        (2, "Product B", 5),
        (3, "Product C", 2),
        (4, "Product D", 8),
        (5, "Product E", 12)
    ], ["id", "product_name", "quantity"])

    # Plot a
