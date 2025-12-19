from pyspark.sql import SparkSession
from pyspark.sql.functions import col, current_timestamp

spark = (
    SparkSession.builder
    .appName("bronze_to_silver_digital_payments")
    .getOrCreate()
)

# ======================
# PATHS
# ======================
bronze_path = "s3a://datalake/delta/digital_payments"
silver_path = "s3a://datalake/delta/silver/digital_payments"

# ======================
# READ BRONZE
# ======================
bronze_df = spark.read.format("delta").load(bronze_path)

# ======================
# TRANSFORM
# ======================
silver_df = (
    bronze_df
    .withColumnRenamed("total_amount", "amount")
    .filter(col("amount") > 0)
    .withColumn("processed_at", current_timestamp())
)

# ======================
# WRITE SILVER (SNAPSHOT)
# ======================
(
    silver_df.write
    .format("delta")
    .mode("overwrite")
    .option("overwriteSchema", "true")
    .save(silver_path)
)

print("✅ Bronze → Silver completed")
spark.stop()
