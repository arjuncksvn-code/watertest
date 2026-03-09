from pyspark.sql import SparkSession
from src.transformations import clean_data

def test_clean_data():
    spark = SparkSession.builder.master("local[*]").getOrCreate()
    df = spark.createDataFrame([(1, "x"), (None, "y"), (1, "x")], ["id", "val"])
    result = clean_data(df)
    assert result.count() == 1
