import matplotlib.pyplot as plt

def plot_data(data):
    """
    Plots the data using matplotlib.

    Args:
        data (DataFrame): The input data as a DataFrame.
    """
    # Extract columns for plotting
    x = data.select("x").rdd.flatMap(lambda x: x).collect()
    y = data.select("y").rdd.flatMap(lambda x: x).collect()

    # Create a scatter plot
    plt.scatter(x, y)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Data Plot")
    plt.show()

if __name__ == "__main__":
    # Initialize SparkSession
    spark = SparkSession.builder \
        .appName("Plotting") \
        .getOrCreate()

    # Sample usage of plot_data function
    data = spark.createDataFrame([
        (1, 10),
        (2, 15),
        (3, 8),
        (4, 12),
        (5, 20)
    ], ["x", "y"])

    # Plot the data
    plot_data(data)

    # Stop the SparkSession
    spark.stop()
