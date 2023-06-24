from pyspark.sql import SparkSession
from utils import helper_functions
from data_processing import data_loader, preprocessing
from visualization import plotting, report_generator

if __name__ == "__main__":
    # Initialize SparkSession
    spark = SparkSession.builder \
        .appName("Data Analysis") \
        .getOrCreate()

    # Load data using data loader
    data = data_loader.load_data(spark, "data.csv")

    # Perform data preprocessing
    preprocessed_data = preprocessing.preprocess_data(data)

    # Generate visualization plots
    plotting.plot_data(preprocessed_data)

    # Generate report
    report_generator.generate_report(preprocessed_data)

    # Perform some operations using helper functions
    result = helper_functions.perform_operations(preprocessed_data)

    # Display the result
    result.show()

    # Stop the SparkSession
    spark.stop()
