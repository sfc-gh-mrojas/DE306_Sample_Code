from pyspark.sql import SparkSession
from pyspark.sql.functions import corr
import common.extractors

# Create a SparkSession
spark = SparkSession.builder.getOrCreate()

# Create sample data
data = [
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
]

columns = ["col1", "col2", "col3"]
df = spark.createDataFrame(data, columns)

# Utility algorithm: Calculate correlation matrix
def calculate_correlation_matrix(dataframe):
    correlation_matrix = {}

    for col1 in dataframe.columns:
        correlations = []
        
        for col2 in dataframe.columns:
            correlation = dataframe.select(corr(col1, col2)).collect()[0][0]
            correlations.append(correlation)
        
        correlation_matrix[col1] = correlations
    
    return correlation_matrix

# Apply utility algorithm to the DataFrame
correlation_matrix = calculate_correlation_matrix(df)

# Display the correlation matrix
print("Correlation Matrix:")
for col, correlations in correlation_matrix.items():
    print(f"{col}: {correlations}")
