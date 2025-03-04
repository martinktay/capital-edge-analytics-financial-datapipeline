import pandas as pd
from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.getOrCreate()


def load_combined_csv(file_path):
    """
    Loads the combined CSV file from Azure Data Lake.
    """
    try:
        # Use Spark to read the file from Azure storage
        df = spark.read.csv(file_path, header=True, inferSchema=True)
        return df.toPandas()
    except Exception:
        # Return an empty DataFrame if the file doesn't exist
        return pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume", "Symbol"])


def save_combined_csv(data, file_path):
    """
    Saves the combined data back to Azure Data Lake in CSV format.
    """
    # Convert pandas DataFrame to Spark DataFrame
    spark_df = spark.createDataFrame(data)
    # Write to Azure Data Lake in CSV format
    spark_df.write.csv(file_path, header=True, mode="overwrite")
    print(f"Data saved to {file_path}")
